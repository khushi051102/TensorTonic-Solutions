def k_means_centroid_update(points, assignments, k):
    """
    Compute new centroids as the mean of assigned points.
    """


    cluster = []
    for i in range(k):
        li = []
        for j in range(len(assignments)):
            if assignments[j] == i:
                li.append(points[j])
        cluster.append(li)

    centroid = []

    for c in cluster:
        num = len(c)

        if num == 0:
            centroid.append([0]*len(points[0]))
            continue

        dim = len(points[0])
        mean = []

        for d in range(dim):
            s = sum(p[d] for p in c)
            mean.append(s/num)

        centroid.append(mean)

    return centroid