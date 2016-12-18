#Original From http://scikit-learn.org/stable/auto_examples/cluster/plot_mean_shift.html#

from Line_Recognizing import The_Featurizer


def main():
    import numpy as np
    from sklearn.cluster import MeanShift, estimate_bandwidth
    from sklearn.datasets.samples_generator import make_blobs
    centers = [[1, 1], [-1, -1], [1, -1]]
    features = The_Featurizer.FeatureExtractor()
    import time
    start = time.time()
    for i in range(334):
        features.featurize("/Users/nickdugal/desktop/pics/horizontal/horizontal" + str(i) + ".jpeg")
    # print(features.features)
    end = time.time()
    print(end - start)
    start= time.time()
    for i in range(333):
        features.featurize("/Users/nickdugal/desktop/pics/vertical/vertical" + str(i) + ".jpeg")

    end = time.time()
    print(end-start)
    start = time.time()
    for i in range(333):
        features.featurize("/Users/nickdugal/desktop/pics/oscilating/wave" + str(i) + ".jpeg")
    X = features.features
    X = np.asarray(X)
    end = time.time()
    print(end-start)
    # The following bandwidth can be automatically detected using
    bandwidth = estimate_bandwidth(X, quantile=0.2, n_samples=5000)

    ms = MeanShift(bandwidth=bandwidth, bin_seeding=True)
    ms.fit(X)
    labels = ms.labels_
    cluster_centers = ms.cluster_centers_

    labels_unique = np.unique(labels)
    n_clusters_ = len(labels_unique)

    print("number of estimated clusters : %d" % n_clusters_)
    import matplotlib.pyplot as plt
    from itertools import cycle

    plt.figure(1)
    plt.clf()

    colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
    for k, col in zip(range(n_clusters_), colors):
        my_members = labels == k
        cluster_center = cluster_centers[k]

        plt.plot(X[my_members, 0], X[my_members, 1], col + '.')
        plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                 markeredgecolor='k', markersize=14)
    plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.show()




if __name__ == "__main__": main()