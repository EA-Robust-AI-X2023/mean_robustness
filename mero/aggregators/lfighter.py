from torch import Tensor

class LFighter:
    """Apply the LFighter aggregator.

    This defense is tailored against label flipping attacks. It applies a clustering
    method on the gradients to filter out potential poisons.
    
    LFighter is suitable in non i.i.d federated learning settings [1]_.

    ## References

    .. [1] Najeeb Moharram Jebreel, Josep Domingo-Ferrer, David Sánchez and Alberto
           Blanco-Justicia. Defending against the Label-flipping Attack in Federated
           Learning. In arXiv, 2022.
    """
    def __init__(self):
        pass

    def aggregate(self, vectors: Tensor):
        raise NotImplementedError