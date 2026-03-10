import numpy as np

def cohens_kappa(rater1, rater2):
    """
    Compute Cohen's Kappa coefficient.
    """
    n = len(rater1)

    # observed agreement
    agree = sum(1 for a, b in zip(rater1, rater2) if a == b)
    p_o = agree / n

    # collect labels
    labels = set(rater1) | set(rater2)

    # count frequencies
    from collections import Counter
    c1 = Counter(rater1)
    c2 = Counter(rater2)

    # expected agreement
    p_e = 0
    for k in labels:
        p_e += (c1[k] / n) * (c2[k] / n)

    # handle degenerate case
    if p_e == 1.0:
        return 1.0
    return (p_o - p_e) / (1 - p_e)