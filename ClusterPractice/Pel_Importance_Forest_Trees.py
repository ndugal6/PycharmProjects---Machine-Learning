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

# Number of cores to use to perform parallel fitting of the forest model
n_jobs = 1

# Load the faces dataset
from create_Dataset2 import  CustomDataSet
dic = dict(data=[], target=[])

for i in range(20):
    dat = dic['data']
    img = misc.imread("/Users/nickdugal/desktop/pics/oscilating/wave{}.jpeg".format(i)) / 255
    w, h, d = original_shape = tuple(img.shape)
    assert d == 4, print(img.shape)
    image_array = np.reshape(img, (w * h, d))
    dat.append(image_array)
    dic['data'] = dat
    tar = dic['target']
    tar.append(0)
    dic['target'] = tar

ds = CustomDataSet()
ds.data = dic['data']
ds.target = dic['target']
X = np.asarray(ds.data)
#data = fetch_olivetti_faces()
X = X.reshape((len(ds.data), -1))
y = np.asarray(ds.target)

mask = y < 5  # Limit to 5 classes
X = X[mask]
y = y[mask]

# Build a forest and compute the pixel importances
print("Fitting ExtraTreesClassifier on faces data with %d cores..." % n_jobs)
t0 = time()
forest = ExtraTreesClassifier(n_estimators=1000,
                              max_features=128,
                              n_jobs=n_jobs,
                              random_state=0)

forest.fit(X, y)
print("done in %0.3fs" % (time() - t0))
importances = forest.feature_importances_
importances = importances.reshape(ds.data[0].shape)

# Plot pixel importances
plt.matshow(importances, cmap=plt.cm.hot)
plt.title("Pixel importances with forests of trees")
plt.show()