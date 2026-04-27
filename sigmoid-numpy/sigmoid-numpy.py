import numpy as np

def sig(x):
    return 1 / (1 + np.exp(-x))
def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    # Write code here
    x = np.array(x)
    return sig(x)
    # if isinstance(x, int):
    #     res = sig(x)
    #     return res
    
    # if isinstance(x, list):
    #     res = []
    #     x = np.array(x)
    #     for i in x:
    #         res.append(sig(i))

    #     return np.array(res)
    # if any(isinstance(a, list) for a in x):
    #     res = []
    #     x = np.array(x)
    #     for i in x:
    #         inner_res = []
    #         for j in i:
    #             print(j)
    #             inner_res.append(sig(j))

    #         res.append(inner_res)

    #     return res
            