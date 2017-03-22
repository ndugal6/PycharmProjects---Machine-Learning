#Original From http://scikit-learn.org/stable/auto_examples/cluster/plot_mean_shift.html#

from Line_Recognizing import The_Featurizer


def main():
    import numpy as np
    import pandas as pd


    from sklearn.cluster import MeanShift, estimate_bandwidth
    from sklearn.datasets.samples_generator import make_blobs
    centers = [[1, 1], [-1, -1], [1, -1]]
    features = The_Featurizer.FeatureExtractor()
    hFeatAgain = pd.read_csv("/Users/nickdugal/desktop/pics/horFeaturesCSV.csv",
                             dtype={'Features': list, 'Target': int})
    for fixMe in hFeatAgain.Features[:9000]:
        fixed = fixMe[1:-1].split()
        features.set_features([float(i[:-1]) for i in fixed])
        features.set_targets(0)

    vFeatAgain = pd.read_csv("/Users/nickdugal/desktop/pics/vertFeaturesCSV.csv",
                             dtype={'Features': list, 'Target': int})
    for fixMe in vFeatAgain.Features[:9000]:
        fixed = fixMe[1:-1].split()
        features.set_features([float(i[:-1]) for i in fixed])
        features.set_targets(1)

    wFeatAgain = pd.read_csv("/Users/nickdugal/desktop/pics/waveFeaturesCSV.csv",
                             dtype={'Features': list, 'Target': int})
    for fixMe in wFeatAgain.Features[:9000]:
        fixed = fixMe[1:-1].split()
        features.set_features([float(i[:-1]) for i in fixed])
        features.set_targets(2)
    doubleHFeat = pd.read_csv("/Users/nickdugal/desktop/pics/doubleHorFeaturesCSV.csv",
                                  dtype={'Features': list, 'Target': int})
    doubleVFeat = pd.read_csv("/Users/nickdugal/desktop/pics/doubleVertFeaturesCSV.csv",
                                  dtype={'Features': list, 'Target': int})
    for fixMe in doubleHFeat.Features[:1000]:
        fixed = fixMe[1:-1].split()
        features.set_features([float(i[:-1]) for i in fixed])
        features.set_targets(0)
    for fixMe in doubleVFeat.Features[:1000]:
        fixed = fixMe[1:-1].split()
        features.set_features([float(i[:-1]) for i in fixed])
        features.set_targets(1)
    X = features.features
    X = np.asarray(X)
    # The following bandwidth can be automatically detected using
    bandwidth = estimate_bandwidth(X, quantile=0.3, n_samples=1000, random_state=0, n_jobs=1)

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
    count = 0
    thePlotData = []
    for k, col in zip(range(n_clusters_), colors):
        my_members = labels == k
        cluster_center = cluster_centers[k]

        thePlot = plt.plot(X[my_members, 0], X[my_members, 1], col + '.', gid=count, picker=5)
        for data in thePlot:
            thePlotData.append(data)
        count = count + 1
        plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col,
                 markeredgecolor='k', markersize=14)

    def on_plot_hover(event):
        for curve in thePlotData:
            print(curve.get_gid())
            print(event.ind)

    plt.figure(1).canvas.mpl_connect('pick_event', on_plot_hover)

    plt.title('Estimated number of clusters: %d' % n_clusters_)
    plt.show()




if __name__ == "__main__": main()