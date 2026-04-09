import numpy as np

def dot_product(x, y):
    """
    Compute the dot product of two 1D arrays x and y.
    Must return a float.
    """

    # Convert to numpy arrays
    x = np.asarray(x)
    y = np.asarray(y)

    # Check 1D
    if x.ndim != 1 or y.ndim != 1:
        raise ValueError("Inputs must be 1D arrays")

    # Check equal length
    if x.shape[0] != y.shape[0]:
        raise ValueError("Vectors must have the same length")

    # Compute dot product (vectorized)
    result = np.dot(x, y)

    return float(result)