def top_k_recommendations(scores, rated_indices, k):
    """
    Return indices of top-k unrated items by predicted score.
    """
    # filter unrated items
    candidates = [(score, i) for i, score in enumerate(scores) if i not in rated_indices]

    # score by descending 
    candidates.sort(key = lambda x: -x[0])

    # take top k indices
    return [i for _, i in candidates[:k]]