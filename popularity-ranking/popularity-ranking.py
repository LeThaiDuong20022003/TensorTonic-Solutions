def popularity_ranking(items, min_votes, global_mean):
    """
    Compute the Bayesian weighted rating for each item.
    """
    result = []

    for R, v in items:
        wr = (v / (v + min_votes)) * R + (min_votes / (v + min_votes)) * global_mean
        result.append(wr)
    return result