import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    """
    Perform one AdaGrad update step.
    """
    # Convert to float
    w = np.asarray(w, dtype = float)
    g = np.asarray(g, dtype = float)
    G = np.asarray(G, dtype = float)

    # Accumulate Squared Gradients
    new_G = G + g ** 2

    # Parameter Update
    new_w = w - lr * g / np.sqrt(new_G + eps)

    return (new_w, new_G)