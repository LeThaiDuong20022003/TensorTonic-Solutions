import numpy as np

def entropy_node(y):
    """
    Compute entropy for a single node using stable logarithms.
    """
    # Return array
    y = np.asarray(y)

    # Handle empty nodes
    if y.size == 0:
        return 0.0

    # Get class counts
    _, counts = np.unique(y, return_counts = True)

    # Compute probability
    prob = counts / sum(counts)

    # Remove zero prob
    prob = prob[prob > 0]

    # Compute entropy
    entropy = - np.sum(prob * np.log2(prob))

    return entropy