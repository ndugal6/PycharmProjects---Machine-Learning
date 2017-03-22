from scipy import misc
import numpy as np
import operator
import matplotlib.pyplot as plt
import pandas as pd
import time


#Normalize values to indicate number of intersections during a horizontal scan of a 100*100pixel image

#TARGET LEGEND
#VERTICAL : 1
#HORIZONTAL : 0
#OSCILLATING : 2
#DOUBLEHORIZONTAL : 3
#DOUBLE VERTICAL : 4
#DOUBLE WAVE : 5
class FeatureExtractor:
    def __init__(self):
        self.features = []
        self.targets = []
        self.filePaths = []

    def features(self):
        return self.features

    def set_features(self, key):
        self.features.append(key)

    def targets(self):
        return self.targets

    def set_targets(self,key):
        self.targets.append(key)

    def set_filepaths(self, filepath):
        self.filePaths.append(filepath)

    def filePaths(self):
        return self.filePaths



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

        width = 0.0
        for rows in maxes:
            if float(rows) != 0.0: width += 1.0
        # Number of intersections/ yields the distance covered if you follow the wave's path aka # of Pixels
        ofMaxes = float(sum(maxes))
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

        # self.set_filepaths(filePath)x
        self.set_features(features)

    def featurizeTargets(self, filePath, target):
        self.set_targets(target)
        self.set_filepaths(filePath)
        self.featurize(filePath)

def main():

    # print(scanning.features)
    print("Hi")
    # print(type(vscanning.features))
    # print(scanning.features)
    # hscanning = FeatureExtractor()
    # hscanning.featurizeTargets("/Users/nickdugal/desktop/pics/horizontal/horizontal1.jpeg",1)
    # print(scanning.features)


    vscanning = FeatureExtractor()
    hscanning = FeatureExtractor()
    oscanning = FeatureExtractor()
    v2scanning = FeatureExtractor()
    tic = time.clock()


    h2scanning = FeatureExtractor()
    k = range(0,20000)
    prevTime = 0.0
    for i in k:
        v2scanning.featurizeTargets("/Users/nickdugal/desktop/pics/doubleVertical/doubleVertical" + str(i) + ".jpeg",4)
        if (i%1000 == 0):
            curTime = time.clock()-tic
            print("Time till ", i, " is", curTime,"seconds(",(curTime)/60,"minutes)\n")
            print("\tTime Difference:",curTime-prevTime,"seconds(",(curTime-prevTime)/60,"minutes)\n")
            prevTime=curTime
    print("Feature lengths", len(v2scanning.features))
    print("Target lengths", len(v2scanning.targets))
    print("Path lengths", len(v2scanning.filePaths))
    doubleVertFeaturesCSV = pd.DataFrame({"Features": v2scanning.features, "Target": v2scanning.targets,
                                    "Path": v2scanning.filePaths}, index=k)
    doubleVertFeaturesCSV.to_csv("/Users/nickdugal/desktop/pics/doubleVertFeaturesCSV.csv")
    oCSVCheck = pd.read_csv("/Users/nickdugal/desktop/pics/doubleVertFeaturesCSV.csv", index_col=0)
    print(oCSVCheck.head())
    print(oCSVCheck.columns)
    print(oCSVCheck.shape)
    # for k in range(2,10):
    #     for i in range(0,1000):
    #         vscanning.featurizeTargets("/Users/nickdugal/desktop/pics/vertical/vertical" + str(i) + ".jpeg")
    #     vertFeaturesCSV = pd.DataFrame({"Features": vscanning.features, "Target": vscanning.targets,
    #                                     "Path": vscanning.filePaths})
    #     vertFeaturesCSV.to_csv("/Users/nickdugal/desktop/pics/vertFeaturesCSV.csv")
    #     comboVFeats = pd.read_csv("/Users/nickdugal/desktop/pics/vertFeaturesCSV.csv")
    #     comboVFeats.append(vertFeaturesCSV)
    #     comboVFeats.to_csv("/Users/nickdugal/desktop/pics/vertFeaturesCSV.csv")
    #
    #     for i in range((k - 1) * 1000, k * 1000):
    #         hscanning.featurizeTargets(
    #             "/Users/nickdugal/desktop/pics/horizontal/horizontal" + str(i) + ".jpeg", 1)
    #     horFeaturesCSV = pd.DataFrame({"Features": hscanning.features, "Target": hscanning.targets}, index=range((k-1)*1000,k*1000))
    #     # horFeaturesCSV.to_csv("/Users/nickdugal/desktop/pics/horFeaturesCSV.csv")
    #     comboHFeats = pd.read_csv("/Users/nickdugal/desktop/pics/horFeaturesCSV.csv")
    #     comboHFeats.append(vertFeaturesCSV)
    #     comboHFeats.to_csv("/Users/nickdugal/desktop/pics/horFeaturesCSV.csv")
    #
    #     for i in range((k - 1) * 1000, k * 1000):
    #         oscanning.featurizeTargets(
    #             "/Users/nickdugal/desktop/pics/oscillating/wave" + str(i) + ".jpeg", 1)
    #     oscFeaturesCSV = pd.DataFrame({"Features": oscanning.features, "Target": oscanning.targets}, index=range((k-1)*1000,k*1000))
    #     # oscFeaturesCSV.to_csv("/Users/nickdugal/desktop/pics/waveFeaturesCSV.csv")
    #     comboOFeats = pd.read_csv("/Users/nickdugal/desktop/pics/waveFeaturesCSV.csv")
    #     comboOFeats.append(vertFeaturesCSV)
    #     comboOFeats.to_csv("/Users/nickdugal/desktop/pics/waveFeaturesCSV.csv")
    #
    #     for i in range((k-1)*1000,k*1000):
    #         v2scanning.featurizeTargets("/Users/nickdugal/desktop/pics/doubleVertical/doubleVertical" + str(i) + ".jpeg",
    #                                    1)
    #     vert2FeaturesCSV = pd.DataFrame({"Features": v2scanning.features, "Target": v2scanning.targets}, index=range((k-1)*1000,k*1000))
    #     # vert2FeaturesCSV.to_csv("/Users/nickdugal/desktop/pics/doubleVertFeaturesCSV.csv")
    #     comboV2Feats = pd.read_csv("/Users/nickdugal/desktop/pics/doubleVertFeaturesCSV.csv")
    #     comboV2Feats.append(vertFeaturesCSV)
    #     comboV2Feats.to_csv("/Users/nickdugal/desktop/pics/doubleVertFeaturesCSV.csv")
    #
    #     for i in range((k-1)*1000,k*1000):
    #         h2scanning.featurizeTargets("/Users/nickdugal/desktop/pics/doubleHorizontal/doubleHorizontal" + str(i) + ".jpeg",
    #                                    1)
    #     hor2FeaturesCSV = pd.DataFrame({"Features": h2scanning.features, "Target": h2scanning.targets}, index=range((k-1)*1000,k*1000))
    #     # hor2FeaturesCSV.to_csv("/Users/nickdugal/desktop/pics/doubleHorFeaturesCSV.csv")
    #     comboH2Feats = pd.read_csv("/Users/nickdugal/desktop/pics/doubleHorFeaturesCSV.csv")
    #     comboH2Feats.append(vertFeaturesCSV)
    #     comboH2Feats.to_csv("/Users/nickdugal/desktop/pics/doubleHorFeaturesCSV.csv")
    #
    #
    #     # comboHFeats = pd.read_csv("/Users/nickdugal/desktop/pics/doubleHorFeaturesCSV.csv")
    #     # comboHFeats.append(horFeaturesCSV)
    #     # comboHFeats.to_csv("/Users/nickdugal/desktop/pics/doubleHorFeaturesCSV.csv")



    # wscanning = FeatureExtractor()
    # for i in range(10000):
    #     wscanning.featurizeTargets("/Users/nickdugal/desktop/pics/oscilating/wave" + str(i) + ".jpeg", 1)
    # vertFeaturesCSV = pd.DataFrame({"Features": wscanning.features,
    #                                 "Target": wscanning.targets})
    # vertFeaturesCSV.to_csv("/Users/nickdugal/desktop/pics/waveFeaturesCSV.csv")
    # print(vertFeaturesCSV.head())
    # print(type(vertFeaturesCSV.Features[0]))
    # import ast
    # vFeatAgain = pd.read_csv("/Users/nickdugal/desktop/pics/vertFeaturesCSV.csv", dtype={'Features' : list, 'Target': int})
    # firstFest = vFeatAgain.Features[0][1:-1].split()
    # for i in firstFest:
    #     print(i)
    # firstFest = [float(i[:-1]) for i in firstFest]
    # print(firstFest)

    # oscanning.featurizeTargets("/Users/nickdugal/desktop/pics/oscilating/wave1.jpeg",2)
    # print("Vertical Features: {}\n Horizontal Features: {}\n Oscilating Features: {}\n Features: Horizontal Maxes, Vertical Maxes, Height, Width".format(vscanning.features, hscanning.features, oscanning.features))
    # print("targets {}, {}, {}".format(vscanning.targets, hscanning.targets,oscanning.targets))
    toc = time.clock()
    print("Time to complete: ", toc-tic, "seconds\n\tOr", (toc-tic)/(60), "minutes.")
if __name__ == "__main__": main()



