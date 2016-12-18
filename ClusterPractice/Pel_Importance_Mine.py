#This example shows the use of forests of trees to evaluate the importance of the pixels in an image classification task (faces).
# The hotter the pixel, the more important.

#The code below also illustrates how the construction and the computation of the predictions can be parallelized within multiple jobs.


print(__doc__)

from time import time
import matplotlib.pyplot as plt

from sklearn.datasets import fetch_olivetti_faces
from sklearn.ensemble import ExtraTreesClassifier
from scipy import misc
import numpy as np
from Line_Recognizing import The_Featurizer

# Number of cores to use to perform parallel fitting of the forest model
n_jobs = 1

test_features = The_Featurizer.FeatureExtractor()
for i in range(334,400):
    test_features.featurizeTargets("/Users/nickdugal/desktop/pics/horizontal/horizontal" + str(i) + ".jpeg",0)
for i in range(333,400):
    test_features.featurizeTargets("/Users/nickdugal/desktop/pics/vertical/vertical" + str(i) + ".jpeg",1)
for i in range(333,400):
    test_features.featurizeTargets("/Users/nickdugal/desktop/pics/oscilating/wave" + str(i) + ".jpeg",2)
X_test = test_features.features
X_test = np.asarray(X_test)
y_test = np.asarray(test_features.targets)

mask = y_test < 5  # Limit to 5 classes
X_test = X_test[mask]
y_test = y_test[mask]

# Build a forest and compute the pixel importances
print("Fitting ExtraTreesClassifier on faces data with %d cores..." % n_jobs)
t0 = time()
forest = ExtraTreesClassifier(n_estimators=1000,
                              max_features=128,
                              n_jobs=n_jobs,
                              random_state=0)

forest.fit(X_test, y_test)
print("done in %0.3fs" % (time() - t0))
importances = forest.feature_importances_
importances = importances.reshape(X_test.shape)

# Plot pixel importances
plt.matshow(importances, cmap=plt.cm.hot)
plt.title("Pixel importances with forests of trees")
plt.show()