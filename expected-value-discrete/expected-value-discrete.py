import numpy as np

def expected_value_discrete(x, p):
    """
    Returns: float expected value
    """
    
    # Return arrays
    x = np.asarray(x, dtype = float)
    p = np.asarray(p, dtype = float)

    # Check shape
    if x.shape != p.shape:
        raise ValueError("Shape of x and p must be match!")

    # Check probabilites sum to 1
    if not np.allclose(np.sum(p), 1.0, atol = 1e-6):
        raise ValueError("Probabilities must sum to 1")

    return float(np.sum(x * p))
