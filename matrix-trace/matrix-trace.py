import numpy as np

def matrix_trace(A):
    """
    Compute the trace of a square matrix (sum of diagonal elements).
    """
    # Write code here
    if not A:
        return []

    row = len(A)
    sum = 0

    for r in range(row):
        sum += A[r][r]

    return sum
