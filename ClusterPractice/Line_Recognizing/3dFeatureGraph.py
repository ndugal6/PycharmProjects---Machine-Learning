#Original From http://scikit-learn.org/stable/auto_examples/cluster/plot_cluster_iris.html#sphx-glr-auto-examples-cluster-plot-cluster-iris-py
print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from Line_Recognizing import The_Featurizer

from sklearn.cluster import KMeans
from sklearn import datasets

features = The_Featurizer.FeatureExtractor()

import time
start = time.time()
for i in range(334):
    features.featurizeTargets("/Users/nickdugal/desktop/pics/horizontal/horizontal" + str(i) + ".jpeg",0)
# print(features.features)
end = time.time()
print(end - start)
start = time.time()
for i in range(333):
    features.featurizeTargets("/Users/nickdugal/desktop/pics/vertical/vertical" + str(i) + ".jpeg",1)

end = time.time()
print(end - start)
start = time.time()
for i in range(333):
    features.featurizeTargets("/Users/nickdugal/desktop/pics/oscilating/wave" + str(i) + ".jpeg",2)

end = time.time()
print(end - start)





np.random.seed(5)

centers = [[1, 1], [-1, -1], [1, -1]]
iris = datasets.load_iris()
# X = iris.data
X = features.features
X = np.asarray(X)
# y = iris.target
y = np.asarray(features.targets)


estimators = {'k_means_iris_3': KMeans(n_clusters=3),
              'k_means_iris_8': KMeans(n_clusters=8),
              'k_means_iris_bad_init': KMeans(n_clusters=3, n_init=1,
                                              init='random')}


fignum = 1
for name, est in estimators.items():
    fig = plt.figure(fignum, figsize=(4, 3))
    plt.clf()
    ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

    plt.cla()
    est.fit(X)
    labels = est.labels_

    ax.scatter(X[:, 0], X[:, 1], X[:, 2], c=labels.astype(np.float))

    ax.w_xaxis.set_ticklabels([])
    ax.w_yaxis.set_ticklabels([])
    ax.w_zaxis.set_ticklabels([])
    ax.set_xlabel('Horizontal Maxes')
    ax.set_ylabel('Vertical Maxes')
    ax.set_zlabel('Line length')
    fignum = fignum + 1

# Plot the ground truth
fig = plt.figure(fignum, figsize=(4, 3))
plt.clf()
ax = Axes3D(fig, rect=[0, 0, .95, 1], elev=48, azim=134)

plt.cla()

for name, label in [('Horizontal', 0),
                    ('Vertical', 1),
                    ('Oscillating', 2)]:
    ax.text3D(X[y == label, 3].mean(),
              X[y == label, 0].mean() + 1.5,
              X[y == label, 2].mean(), name,
              horizontalalignment='center',
              bbox=dict(alpha=.5, edgecolor='w', facecolor='w'))
# Reorder the labels to have colors matching the cluster results
y = np.choose(y, [1, 2, 0]).astype(np.float)
ax.scatter(X[:, 3], X[:, 0], X[:, 2], c=y)

ax.w_xaxis.set_ticklabels([])
ax.w_yaxis.set_ticklabels([])
ax.w_zaxis.set_ticklabels([])
ax.set_xlabel('Hor Maxes')
ax.set_ylabel('Ver Maxes')
ax.set_zlabel('Line length')
plt.show()