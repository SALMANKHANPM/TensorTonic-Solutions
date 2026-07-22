import numpy as np

def relu(x):
    """
    Implement ReLU activation function.
    """
    def cal_relu(k):
        return max(0, k)

    def apply(v):
        if isinstance(v, (list, tuple, np.ndarray)):
            return [apply(u) for u in v]
        return cal_relu(v)

    return np.asarray(apply(x))
