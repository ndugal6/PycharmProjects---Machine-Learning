from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics

print(__doc__)

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from Line_Recognizing import The_Featurizer

from sklearn.cluster import KMeans
from sklearn import datasets
import pandas as pd

features = The_Featurizer.FeatureExtractor()

hFeatAgain = pd.read_csv("/Users/nickdugal/desktop/pics/horFeaturesCSV.csv", dtype={'Features' : list, 'Target': int})
for fixMe in hFeatAgain.Features[:9000]:
    fixed = fixMe[1:-1].split()
    features.set_features([float(i[:-1]) for i in fixed])
    features.set_targets(0)

vFeatAgain = pd.read_csv("/Users/nickdugal/desktop/pics/vertFeaturesCSV.csv", dtype={'Features' : list, 'Target': int})
for fixMe in vFeatAgain.Features[:9000]:
    fixed = fixMe[1:-1].split()
    features.set_features([float(i[:-1]) for i in fixed])
    features.set_targets(1)

wFeatAgain = pd.read_csv("/Users/nickdugal/desktop/pics/waveFeaturesCSV.csv", dtype={'Features' : list, 'Target': int})
for fixMe in wFeatAgain.Features[:9000]:
    fixed = fixMe[1:-1].split()
    features.set_features([float(i[:-1]) for i in fixed])
    features.set_targets(2)
doubleHFeat = pd.read_csv("/Users/nickdugal/desktop/pics/doubleHorFeaturesCSV.csv", dtype={'Features' : list, 'Target': int})
doubleVFeat = pd.read_csv("/Users/nickdugal/desktop/pics/doubleVertFeaturesCSV.csv", dtype={'Features' : list, 'Target': int})
X = features.features
X = np.asarray(X)
y = np.asarray(features.targets)

test_features = The_Featurizer.FeatureExtractor()
for fixMe in doubleHFeat.Features[:1000]:
    fixed = fixMe[1:-1].split()
    test_features.set_features([float(i[:-1]) for i in fixed])
    test_features.set_targets(0)
for fixMe in doubleVFeat.Features[:1000]:
    fixed = fixMe[1:-1].split()
    test_features.set_features([float(i[:-1]) for i in fixed])
    test_features.set_targets(1)
for fixMe in wFeatAgain.Features[9000:10000]:
    fixed = fixMe[1:-1].split()
    test_features.set_features([float(i[:-1]) for i in fixed])
    test_features.set_targets(2)
print(test_features.filePaths)


X_test = test_features.features
X_test = np.asarray(X_test)
y_test = np.asarray(test_features.targets)

clf = MultinomialNB(alpha=.01)
clf.fit(X, y)
pred = clf.predict(X_test)
results = metrics.f1_score(y_test, pred, average='macro')
accuracy = metrics.accuracy_score(y_test,pred)
print("F-score: {}".format(results))
print("Accuracy: {}".format(accuracy))



def show_top10(classifier, vectorizer, categories):
    feature_names = np.asarray(vectorizer.get_feature_names())
    for i, category in enumerate(categories):
        top10 = np.argsort(classifier.coef_[i])[-10:]
        print("%s: %s" % (category, " ".join(feature_names[top10])))