from math import sqrt
from typing import List

import torch
from torch import Tensor

from piefs.morphology import binary_convolution
from piefs.kernels import update3d


def _update_3d(minimum_paired: Tensor, f: float) -> Tensor:
    """
    Partial Psi from one direction of connected components.
    Should only be called from eikonal_single_step on a 3D image.

    Inspired by Kevin Cutler from Omnipose, adapted by Chris Buswinka.

    Notable observations based on the paper https://arxiv.org/pdf/2106.15869.pdf
    "Improved Fast Iterative Algorithm for Eikonal Equation for GPU Computing" by Yuhao Huang, Aug 3 2021:
        - 1; The authors of this paper report multiple different psi update steps based on the relationship of the axis pairs. I.e. if |a2 - a1| < δ,  do this... ELSE |a2 - a1| < -δ do that... This implementation of a solution (and original omnipose) to the eikonal function DOES NOT take into account these conditions.
        - 2; The 2D implementation here, does not work for 3D -- the values explode. Rather, the 3D implementation must be added explicitly. You'd only notice this for big objects, something omnipose skirts around.
        - 3; The values used from the 3D step implementation does not work, I had to bump the scaling term up to 12 (from 6)
        - 4; The original algorithm does not check ordinal axes, and obviously omnipose works just fine, so maybe the point 1 exclusion was intentional.

    Shapes:
        - minimum_paired: (N_pairs, B, C, X, Y, Z)
        - return (B, C, X, Y, Z)

    :param minimum_paired: minimums from eikonal_single_step.
    :param f: distance of pair from the central pixel

    :return: partial psi for that neighborhood.
    """
    minimum_paired, _ = torch.sort(minimum_paired, dim=0)

    a0 = minimum_paired[0, ...]
    a1 = minimum_paired[1, ...]
    a2 = minimum_paired[2, ...]

    case0 = torch.abs(a0 - a2).lt(1)
    case1 = torch.abs(a0 - a1).lt(1) * torch.logical_not(case0)
    case2 = torch.logical_not(torch.logical_or(case0, case1))

    out = torch.zeros_like(a0)

    sum_a = minimum_paired.sum(dim=0)
    sum_a2 = (minimum_paired**2).sum(dim=0)

    # Case 0
    out[case0] = (
        2 * sum_a[case0]
        + torch.sqrt((4 * sum_a[case0].pow(2)) - (12 * (sum_a2[case0] - 1 / (f**2))))
    ).div(6)

    # Case 1
    out[case1] = (
        a0[case1]
        + a1[case1]
        + torch.sqrt((2 / (f**2)) - (a0[case1] - a1[case1]) ** 2)
    ).div(2)

    # Case 2
    out[case2] = a0[case2] + 1 / f

    return out


def _update_2d(minimum_paired: Tensor, f: float) -> Tensor:
    """
    Partial Psi from one direction of connected components.
    Should only be called from eikonal_single_step.

    Inspired by Kevin Cutler from Omnipose, adapted by Chris Buswinka.

    Notable observations based on the paper https://arxiv.org/pdf/2106.15869.pdf
    "Improved Fast Iterative Algoorithm for Eikonal Equation for GPU Computing" by Yuhao Huang, Aug 3 2021:
        - 1; The authors of this paper report multiple different psi update steps based on the relationship of the axis pairs. I.e. if |a2 - a1| < δ,  do this... ELSE |a2 - a1| < -δ do that... This implementation of a solution (and original omnipose) to the eikonal function DOES NOT take into account these conditions.
        - 2; The 2D implementation here, does not work for 3D -- the values explode. Rather, the 3D implementation must be added explicitly. You'd only notice this for big objects, something omnipose skirts around.
        - 3; The values used from the 3D step implementation does not work, I had to bump the scaling term up to 12 (from 6)
        - 4; The original algorithm does not check ordinal axes, and obviously omnipose works just fine, so maybe the point 1 exclusion was intentional.

    Shapes:
        - minimum_paired: (N_pairs, B, C, ...)
        - return (B, C, ...)

    :param minimum_paired: minimums from eikonal_single_step.
    :param f: distance of pair from the central pixel

    :return: partial psi for that neighborhood.
    """

    # Four necessary channels, remaining num are spatial dims...
    d: int = len(minimum_paired.shape) - 3
    minimum_paired, _ = torch.sort(minimum_paired, dim=0)

    a = minimum_paired * (torch.abs(minimum_paired - minimum_paired[-1, ...]) < f)
    sum_a = a.sum(dim=0)
    sum_a2 = (a**2).sum(dim=0)
    # sorting was the source of the small artifact bug

    out = sum_a + torch.sqrt(torch.clamp((sum_a**2) - d * (sum_a2 - f**2), min=0))
    out.div_(2)

    return out


def eikonal_single_step(connected_components: Tensor) -> Tensor:
    """
    Returns the output of one iteration of an eikonal equation.

    This could be a great kernel in triton... you could basically do everything in one 3x3 convolution.
    That would be huge. Maybe a nice weekend project? It'd save an insane amount of memory. I dont think you
    could effectively cache that data though, so it'd be shit efficient, but would save 30Gb of VRAM though.

    YOU CANNOT RUN 3D IN ANY STABILITY WITH THE ALGORITHM AS IS...

    Shapes:
        - connected_components: (B, C, N_components=9, X, Y) or (B, C, N_components=27, X, Y, Z)
        - returns: (B, C, X, Y) or (B, C, X, Y, Z)

    :param connected_components: The connected components of the previous step of the eikonal update function.
    :return: the result of the next step of a solution to the eikonal equation.
    """
    n_spatial_dims = connected_components.ndim - 3

    # The solution needs to understand which connected pixel of affinity graph are how far from the central pixel
    # Omnipose generalizes this to ND. I am not smart enough to do this.
    if n_spatial_dims == 2:  # 2D
        factors: List[float] = [0.0, 1.0, sqrt(2)]
        index_list: List[List[int]] = [[4], [1, 3, 5, 7], [0, 2, 6, 8]]

    elif n_spatial_dims == 3:  # 3D
        factors: List[float] = [0.0, 1.0, sqrt(2), sqrt(3)]
        index_list: List[List[int]] = [  # You can only check cardinal directions!
            [13],
            [4, 10, 12, 14, 16, 22],
        ]
    else:
        raise RuntimeError(
            f"Number of dimensions: {len(connected_components.shape) - 3} is not supported."
        )

    if n_spatial_dims == 2:
        phi = torch.ones_like(connected_components[:, :, 0, ...])

    # find the minimum of each hypercube pair along each axis.
    for ind, f in zip(index_list[1:], factors[1:]):
        n_pair = len(ind) // 2
        minimum_paired = torch.stack(
            [
                torch.minimum(
                    connected_components[:, :, ind[i], ...],
                    connected_components[:, :, ind[-(i + 1)], ...],
                )
                for i in range(n_pair)
            ]
        )

        phi = (
            phi * _update_2d(minimum_paired, f)
            if n_spatial_dims == 2
            else _update_3d(minimum_paired, f)
        )

    # For 2D you can scale appropriately, not with omnipose...
    phi = torch.pow(phi, 1 / (len(index_list) - 1)) if n_spatial_dims == 2 else phi

    return phi


@torch.no_grad()
def solve_eikonal(
    instance_mask: Tensor, eps: float = 1e-3, min_steps: int = 200, use_triton: bool = True
) -> Tensor:
    """
    Solves the eikonal equation on a collection of instance masks. In practice, generates
    a specialized distance mask for each instance of an object in an image. Input may be a 2D or 3D image.

    Possible Optimization: omnipose tracks only the filled values of the mask for the affinities,
    it may be possible for me to do the same for a memory reduction.

    Shapes:
        - instance_mask (B, C, X, Y) or (B, C, X, Y, Z)
        - solution to eikonal function (B, C, X, Y) or (B, C, X, Y, Z)

    Data Types:
        - instance_mask: int
        - returns: float

    Examples:
        >>> import torch
        >>>
        >>> image = torch.load('path/to/my/image.pt')  # An image with shape (B, C, X, Y, Z)
        >>> eikonal = solve_eikonal(image)

    :param instance_mask: Input mask with instances denoted by integers and zero as background
    :param eps: Minimum tolerable error to eikonal function
    :param min_steps: Minimum number of iterations to solve eikonal function
    :param use_triton: If true, uses a fused cuda kernel for eikonal solving 3D masks
    :return: Solution to eikonal function. Basically a fancy smooth distance map.
    """

    assert instance_mask.ndim == 5, 'instance_mask must be a 5D tensor: [B, C, X, Y, Z]'

    if use_triton:
        assert instance_mask.is_cuda, 'instance_mask must be a cuda tensor if use_triton=True'
        # assert instance_mask.shape[0] == 1, 'instance_mask must have a batch size of 1 if use_triton=True'
        assert instance_mask.shape[1] == 1, 'instance_mask must have a channel size of 1 if use_triton=True'
        assert instance_mask.dtype == torch.float32, 'instance_mask must be float32 if use_triton=True'

        out = []
        for b in range(instance_mask.shape[0]):
            _batch_mask = instance_mask[b, 0, ...]
            T = torch.ones_like(_batch_mask) * _batch_mask.gt(0)
            error = float('inf')
            t = 0
            while error > eps and t < min_steps:
                T0 = update3d(T, _batch_mask)
                T = update3d(T0, _batch_mask)
                error = (T - T0).square().mean()
                t += 1
                if t > 500:
                    raise RuntimeError('maximum iterations exceded')
            out.append(T.unsqueeze(0).unsqueeze(0))
        return torch.cat(out, dim=0)

    # Get the values of adjacent pixels of the input image.
    # Returns a (B, C, N, X, Y, Z?) image where N=9 for a 2D image, and 27 for a 3D image.
    affinity_mask: Tensor = binary_convolution(instance_mask, padding_mode="replicate")

    # Remove all connections to pixels with different labels from center
    affinity_mask[affinity_mask != instance_mask.unsqueeze(2)] = 0.0

    # Mask for removing updates to background pixels
    affinity_mask = affinity_mask.gt(0)

    T, T0 = torch.ones_like(instance_mask), torch.ones_like(instance_mask)

    t = 0
    error = float("inf")

    while error > eps and t < min_steps:  # Loop is a hard bottleneck...
        T: Tensor = eikonal_single_step(
            binary_convolution(T, "replicate") * affinity_mask
        )

        error = (T - T0).square().mean()

        T0.copy_(T)
        t += 1
        if t > 500:
            raise RuntimeError('maximum iterations exceded')

    return T


def gradient_from_eikonal(eikonal: Tensor) -> Tensor:
    """
    Calculates the gradient of a distance field calculated by solving the eikonal distance function.

    Uses a lot of shape manipulation to vectorize the code and leverage a 1D convolution.
    Im almost certain im doing some scaling wrong. Unclear as to how.
    The images look close enough though

    Shapes:
        - eikonal: (B, C=1, X, Y) or (B, C=1, X, Y, Z)
        - returns: (B, N_dim=2, X, Y) or (B, N_dim=3, X, Y, Z)

    N_dim is the components of the gradient vector. Either (X, Y) or (X, Y, Z)

    :param eikonal: eikonal distance field calculated by solve_eikonal
    :return: components of gradients of eikonal distance field.
    """
    spatial_dim = eikonal.ndim - 2  # [B, C, X, Y] or [B, C, X, Y, Z]

    if spatial_dim < 2 or spatial_dim > 3:
        raise RuntimeError(
            f"Spatial Dimension of {spatial_dim} is not supported: {eikonal.shape}"
        )

    # For the gradient calculation, we need to know if the adjacent pixels are above,
    # below, or next to the base pixel...
    vector_direction = torch.zeros(  # [9, 2] or [27, 3] array
        (3**spatial_dim, spatial_dim), device=eikonal.device, dtype=torch.long
    )
    ind = 0
    for k in (1, 0, -1) if spatial_dim == 3 else (0,):
        for j in (-1, 0, 1):
            for i in (-1, 0, 1):
                vector_direction[ind, 0] = i
                vector_direction[ind, 1] = j
                if spatial_dim == 3:
                    vector_direction[ind, 2] = k

                ind += 1

    # 27 or 9 tensor
    # 0, 1, 1.41, 1.713... or something idk
    vector_magnitude = vector_direction.abs().sum(dim=1).float()
    vector_magnitude[vector_magnitude != 0].sqrt_()

    # gets rid of divide by zero issue
    vector_magnitude[vector_magnitude == 0] = float("inf")
    vector_magnitude.mul_(2).pow_(2)  # necessary for proper gradient scaling

    # [B, C, N=9 or 27, 1, ...]
    affinities: Tensor = binary_convolution(eikonal, padding_mode="replicate")

    affinities.sub_(eikonal.unsqueeze(1))  # get difference...

    shape: List[int] = list(eikonal.shape)

    gradient = []

    # Reshapes for 1D convolution.
    # New Shape -> [B, 9, X*Y] if 2D, [B, 27, X*Y*Z] if 3D
    affinities = affinities.transpose(1, 2).reshape(shape[0], 3**spatial_dim, -1)

    for dim in range(spatial_dim):
        kernel: Tensor = (
            vector_direction[:, dim].view(1, -1, 1).div(vector_magnitude.view(1, -1, 1))
        )

        partial_gradient = F.conv1d(affinities, kernel)

        gradient.append(partial_gradient.reshape(shape[0], 1, *shape[2::]))

    return torch.concat(gradient, dim=1)


    # Copyright Chris Buswinka, 2023
