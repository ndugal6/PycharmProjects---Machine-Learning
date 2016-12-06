from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

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

X = features.features
X = np.asarray(X)
y = np.asarray(features.targets)

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

clf = MultinomialNB(alpha=.01)
clf.fit(X, y)
pred = clf.predict(X_test)
results = metrics.f1_score(y_test, pred, average='macro')
print("F-score: {}".format(results))


def show_top10(classifier, vectorizer, categories):
    feature_names = np.asarray(vectorizer.get_feature_names())
    for i, category in enumerate(categories):
        top10 = np.argsort(classifier.coef_[i])[-10:]
        print("%s: %s" % (category, " ".join(feature_names[top10])))