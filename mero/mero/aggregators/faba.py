from torch import Tensor

class FABA:
    """Apply the FABA aggregator.

    This algorithm iteratively removes outliers and computes the mean of the resulting
    vectors [1]_.

    ## References

    .. [1] Qi Xia, Zeyi Tao, Zijiang Hao, Qun Li. FABA: An Algorithm for Fast Aggregation
           against Byzantine Attacks in Distributed Neural Networks. In International
           Joint Conference on Artificial Intelligence, pp. 4824-4830. IJCAI, 2019.
    """
    def __init__(self):
        pass

    def aggregate(self, vectors: Tensor):
        raise NotImplementedError