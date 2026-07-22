import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    def cal_sig(u):
        return  1/ (1 + (np.exp(-u)))
    # Write code here
    if type(x) == type([]) and len(x) != 1:
        val = list()
        for v in x:
            if type(v) == type([]):
                k = []
                for m in v:
                    k.append(cal_sig(m))
                val.append(k)
                k = []
            else:  
                val.append(cal_sig(v))

        return val
    else:
        return cal_sig(x)
        