import numpy as np

def matrix_transpose(A):
    """
    Return the transpose of matrix A (swap rows and columns).
    """
    A = np.asarray(A)
    m, n = A.shape

    # Create new array with swapped shape
    result = np.zeros((n, m), dtype = A.dtype)

    # Manual transpose
    for i in range(m):
        for j in range(n):
            result[j, i] = A[i, j]

    return result