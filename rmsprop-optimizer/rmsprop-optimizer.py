import numpy as np

def rmsprop_step(w, g, s, lr=0.001, beta=0.9, eps=1e-8):
    """
    Perform one RMSProp update step.
    """
    # Convert to arrays
    w = np.asarray(w)
    g = np.asarray(g)
    s = np.asarray(s)

    # Update w, s
    s_new = beta * s + (1 - beta) * (g ** 2)
    w_new = w - lr * g / np.sqrt(s_new + eps)

    # Return result
    return (w_new, s_new)