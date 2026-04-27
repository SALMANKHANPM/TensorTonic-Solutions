import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    # Write code here
    if not A:
        return []

    rows = len(A)
    cols = len(A[0])

    transposed = []
    for c in range(cols):
        inner = []
        for r in range(rows):
            inner.append(A[r][c])
        transposed.append(inner)

    return np.array(transposed)