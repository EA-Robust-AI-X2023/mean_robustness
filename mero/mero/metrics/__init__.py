"""
# Gradient metrics

This module implements some gradient metrics in federated learning as in Peng et. al. [1]_.

## References

.. [1] Jie Peng, Weiyu Li, Stefan Vlaski, Qing Ling. Mean Aggregator is More Robust than
       Robust Aggregators under Label Poisoning Attacks on Distributed Heterogeneous Data.
       In International Joint Conference on Artificial Intelligence, pp. 4797-4805. IJCAI, 2024.
"""

import torch
from torch import Tensor


@torch.no_grad()
def heterogeneity(regular_gradients: list[Tensor], global_gradient: Tensor) -> float:
    """Compute the heterogeneity of the regular gradients.

    Args:
        regular_gradients (list[Tensor]): The local gradients of the regular workers.
        global_gradient (Tensor): The global gradient aggregated from all workers,
            including byzantine nodes.

    Returns:
        xi (float): The maximum distance between a regular gradient and the global gradient.
    """
    raise NotImplementedError

@torch.no_grad()
def disturbance(poisoned_gradients: list[Tensor], global_gradient: Tensor) -> float:
    """Compute the disturbance caused by the poisoned gradients.

    Args:
        poisoned_gradients (list[Tensor]): The local gradients of the byzantine workers.
        global_gradient (Tensor): The global gradient aggregated from all workers,
            including regular and byzantine nodes.

    Returns:
        A (float): The maximum distance between a poisoned gradient and the global gradient.
    """
    return heterogeneity(poisoned_gradients, global_gradient)

@torch.no_grad()
def inner_var(per_sample_gradients: list[Tensor], local_gradient: Tensor) -> float:
    """Compute the inner variance of the per-sample gradients of one worker.

    Args:
        per_sample_gradients (list[Tensor]): The local per-sample gradients of one worker.
        local_gradient (Tensor): The local aggregated gradient of the worker.

    Returns:
        sigma_2 (float): The inner variance.
    """
    raise NotImplementedError