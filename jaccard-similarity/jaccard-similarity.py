def jaccard_similarity(set_a, set_b):
    """
    Compute the Jaccard similarity between two item sets.
    """
    a,b=set(set_a),set(set_b)
    inter=len(a&b)
    un=len(a|b)
    if un==0:
        return 0.0
    return inter/un