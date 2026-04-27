import numpy as np

def bernoulli_pmf_and_moments(x, p):
    """
    Compute Bernoulli PMF and distribution moments.
    """
    # Write code here
    pmf = []
    for t in x:
        if t == 1:
            pmf.append(p)
        elif t == 0:
            pmf.append(1-p)


    mean = p
    var = p * ( 1 - p)

    return (np.array(pmf), mean, var)