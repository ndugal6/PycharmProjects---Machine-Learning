# read in the iris data
from sklearn.datasets import load_iris
from create_Dataset2 import  CustomDataSet
import numpy as np
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.metrics import pairwise_distances_argmin
from sklearn.datasets import load_sample_image
from sklearn.utils import shuffle
from time import time
from scipy import misc

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



#iris = load_iris()

# create X (features) and y (response)

X = ds.data
#sum(sum(X,[]),[])

#c, f, r = org_shape = tuple(np.shape(X))
#newX = np.reshape(X,(c,f))
y = ds.target


# import the class

from sklearn.linear_model import LogisticRegression

# instantiate the model (using the default parameters)
logreg = LogisticRegression()

# fit the model with data
print(type(X))
print(np.shape(X))

import itertools as it
                            # a=[]

                            # for i in range(len(X)):
                                # b=[[]]
                                # for j in range(len(X[i])-1):
                            #         b.append(all(range(len(X[i][j]))))
                                    #
                            # a.append(b)
                                # print(type(a))
                                # print(np.shape(a))
                                # X = a.copy()



print(np.shape(X))
print(np.shape(y))
logreg.fit(X, y)

# predict the response values for the observations in X

logreg.predict(X)

# store the predicted response values

y_pred = logreg.predict(X)

# check how many predictions were generated
len(y_pred)


# compute classification accuracy for the logistic regression model
from sklearn import metrics
print(metrics.accuracy_score(y, y_pred))

from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X, y)
y_pred = knn.predict(X)
print(metrics.accuracy_score(y, y_pred))

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X, y)
y_pred = knn.predict(X)
print(metrics.accuracy_score(y, y_pred))

# print the shapes of X and y
print(X.shape)
print(y.shape)

# STEP 1: split X and y into training and testing sets
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=4)


# print the shapes of the new X objects
print(X_train.shape)
print(X_test.shape)

# print the shapes of the new y objects
print(y_train.shape)
print(y_test.shape)


# STEP 2: train the model on the training set
logreg = LogisticRegression()
logreg.fit(X_train, y_train)


# STEP 3: make predictions on the testing set
y_pred = logreg.predict(X_test)

# compare actual response values (y_test) with predicted response values (y_pred)
print(metrics.accuracy_score(y_test, y_pred))

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred))

knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
print(metrics.accuracy_score(y_test, y_pred))

# try K=1 through K=25 and record testing accuracy
k_range = list(range(1, 26))
scores = []
for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    scores.append(metrics.accuracy_score(y_test, y_pred))

# import Matplotlib (scientific plotting library)
import matplotlib.pyplot as plt

# allow plots to appear within the notebook

# plot the relationship between K and testing accuracy
plt.plot(k_range, scores)
plt.xlabel('Value of K for KNN')
plt.ylabel('Testing Accuracy')
plt.show()

# instantiate the model with the best known parameters
knn = KNeighborsClassifier(n_neighbors=11)

# train the model with X and y (not X_train and y_train)
knn.fit(X, y)

# make a prediction for an out-of-sample observation
knn.predict([[3, 5, 4, 2]])