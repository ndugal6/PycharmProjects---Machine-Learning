import matplotlib.pyplot as plt
from sklearn import datasets, metrics, svm
from scipy import misc
import numpy as np

class ImgDataSet:
    def __init__(self):
        #self.properties = {'images': np.array([self.getIms()]), 'targets': [0]}
        dic = dict(data=[], target=[0])
        for i in range(20):
            dat = dic['data']
            theImage = "/Users/nickdugal/desktop/pics/oscilating/wave{}.jpeg".format(i)
            imAr = dic['images']
            img = misc.imread(theImage) / 255
            w, h, d = original_shape = tuple(img.shape)
            assert d == 4, print(img.shape)
            image_array = np.reshape(img, (w * h, d))
            dat.append(image_array)
            dic['data'] = dat
            tar = dic['target']
            tar.append(0)
            dic['target'] = tar
        # self.properties = kwargs
    @property
    def images(self):
        return self.properties.get('images', None)
    @property
    def target(self):
        return self.properties.get('targets', None)
    @images.setter
    def images(self, im):
        self.properties['images'].append(im)
    @target.setter
    def target(self, tar):
        self.properties['images'].append(tar)





    def getIms(self):
        for i in range(20):
            dat = dic['data']
            img = misc.imread("/Users/nickdugal/desktop/pics/oscilating/wave{}.jpeg".format(i)) / 255

        # im2 = misc.imread("/Users/nickdugal/desktop/pics/horizontal/horizontal1.png")
        # im3 = misc.imread("/Users/nickdugal/desktop/pics/oscillating/wave1.png")
        # return np.array([im1, im2, im3])

    def get_properties(self):
        return self.properties

    def get_property(self, key):
        return self.properties.get(key, None)

def main():
    lines = ImgDataSet()
    # lines.images =
    images_and_labels = list(zip(lines.images, lines.target))
    for index, (image, label) in enumerate(images_and_labels[:4]):
        plt.subplot(2, 4, index + 1)
        plt.axis('off')
        plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
        plt.title('Training: %i' % label)

    # To apply a classifier on this data, we need to flatten the image, to
    # turn the data in a (samples, feature) matrix:
    n_samples = len(lines.images)
    data = lines.images.reshape((n_samples, -1))

    # Create a classifier: a support vector classifier
    classifier = svm.SVC(gamma=0.001)

    # We learn the digits on the first half of the digits
    classifier.fit(data[:n_samples / 2], lines.target[:n_samples / 2])

    # Now predict the value of the digit on the second half:
    expected = lines.target[n_samples / 2:]
    predicted = classifier.predict(data[n_samples / 2:])

    print("Classification report for classifier %s:\n%s\n"
          % (classifier, metrics.classification_report(expected, predicted)))
    print("Confusion matrix:\n%s" % metrics.confusion_matrix(expected, predicted))

    images_and_predictions = list(zip(lines.images[n_samples / 2:], predicted))
    for index, (image, prediction) in enumerate(images_and_predictions[:4]):
        plt.subplot(2, 4, index + 5)
        plt.axis('off')
        plt.imshow(image, cmap=plt.cm.gray_r, interpolation='nearest')
        plt.title('Prediction: %i' % prediction)

    plt.show()

if __name__ == "__main__": main()
