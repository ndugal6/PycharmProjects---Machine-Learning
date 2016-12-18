from scipy import misc
import numpy as np
import operator
import matplotlib.pyplot as plt


#Normalize values to indicate number of intersections during a horizontal scan of a 100*100pixel image
class FeatureExtractor:
    def __init__(self):
        self.features = []
        self.targets = []

    def features(self):
        return self.features

    def set_features(self, key):
        self.features.append(key)

    def targets(self):
        return self.targets

    def set_targets(self,key):
        self.targets.append(key)



    def fix_values(self, pixelMisses):
        return 98 - pixelMisses

    def horizontalScan(self, filePath):
        def fix_values(pixelMisses):
            return 98 - pixelMisses
        imPixels = misc.imread(filePath, flatten=True)
        maxes = []
        for ind in range(100):
            maxes.append(0.0)

        past = 0.0
        next = 0.0
        count = 0
        # Finds values for HORIZONTAL SCAN
        for i in imPixels:
            past = float(i[0])
            for idx, num in enumerate(i[1:-1]):
                next = float(i[idx + 1])
                if past <= num and num >= next:
                    maxes[count] += 1
                past = float(num)
            count = count + 1
        maxes = list(map(fix_values, maxes))
        waveHeight = 0

        for rows in maxes:
            if (float(rows) != 0): waveHeight += 1
        amplitude = waveHeight/2;
        # print("Height : {}".format(waveHeight))
        #Number of intersections/ yields the distance covered if you follow the wave's path aka # of Pixels
        intersections = sum(maxes)
        # print("Image has {} maxes".format(intersections))
        return waveHeight, intersections

    def verticalScan(self, filePath):

        imPixels = misc.imread(filePath, flatten=True)
        maxes = []
        for ind in range(100):
            maxes.append(0.0)

        past = 0.0
        next = 0.0
        count = 0
        # Finds values for Vertical SCAN
        maxIndex = 0
        for column in range(len(imPixels[:][:])):
            for row in range(len(imPixels[:])):
                if float(row) == 0.0:
                    past = imPixels[row][column]
                    continue
                if float(row) == len(imPixels[:])-1:
                    break
                current = imPixels[row][column]
                next = imPixels[row+1][column]
                if current >= past:
                    if current >= next:
                        maxes[maxIndex] += 1.0
                past = current
            maxIndex += 1
        maxes = list(map(self.fix_values, maxes))
        # print(maxes)

        width = 0
        for rows in maxes:
            if float(rows) != 0.0: width += 1
        # Number of intersections/ yields the distance covered if you follow the wave's path aka # of Pixels
        ofMaxes = sum(maxes)
        # print("Width : {}".format(width))
        # print("Image has {} maxes".format(ofMaxes))
        amplitude = width / 2
        return width, ofMaxes

    def featurize(self, filePath):
        height, horMax = self.horizontalScan(filePath)
        width, verMax = self.verticalScan(filePath)
        # features = [height, horMax, width, verMax]
        # features = [horMax, verMax, height*width]
        features = [horMax, verMax, height, width]
        # features = [horMax,verMax]
        self.set_features(features)

    def featurizeTargets(self, filePath, target):
        self.set_targets(target)
        self.featurize(filePath)

def main():
    vscanning = FeatureExtractor()
    # print(scanning.features)
    vscanning.featurizeTargets("/Users/nickdugal/desktop/pics/vertical/vertical1.jpeg",0)
    # print(scanning.features)
    hscanning = FeatureExtractor()
    hscanning.featurizeTargets("/Users/nickdugal/desktop/pics/horizontal/horizontal1.jpeg",1)
    # print(scanning.features)
    oscanning = FeatureExtractor()
    oscanning.featurizeTargets("/Users/nickdugal/desktop/pics/oscilating/wave1.jpeg",2)
    print("Vertical Features: {}\n Horizontal Features: {}\n Oscilating Features: {}\n Features: Horizontal Maxes, Vertical Maxes, Height, Width".format(vscanning.features, hscanning.features, oscanning.features))
    print("targets {}, {}, {}".format(vscanning.targets, hscanning.targets,oscanning.targets))

if __name__ == "__main__": main()



