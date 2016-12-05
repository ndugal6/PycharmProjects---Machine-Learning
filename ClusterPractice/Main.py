from PIL import Image
import numpy as np
import csv
import dataset as ds
from struct import *
import scipy.misc as msc
import pandas as pd
def load_image( filename ) :
    im = Image.open(filename)
    return np.asarray(im)
vertArray = []
va = [1,2]
vb = [2,3]
vertArray.append(va)
vertArray.append(vb)
print(vertArray)
# nameBegin = "/Users/nickdugal/desktop/pics/vertical/vertical"
# nameEnd = ".png"
# print(nameBegin,0,nameEnd)
# np_dictionary = {'The_Dealeo':msc.imread(nameBegin + str(0) + nameEnd).flatten()}
# for extension in range(0,20):
#     np_dictionary[str(extension)] = msc.imread(nameBegin + str(extension) + nameEnd).flatten()


    # vertArray.insert(0,msc.imread(nameBegin + str(extension) + nameEnd))
# np_list = np.asarray(vertArray)

# datafram = pd.DataFrame(np_dictionary)
# datafram.to_csv('first.csv')
# vert_np_array = np.array(vertArray)
# np.savetxt("foo.csv", vert_np_array[1,...], delimiter=",",fmt='%.18e')


# example = vert_np_array([[[i for i in range(0, 5)],[0 for j in range(0, 5)]] for k in range(0, 10)])
# f = open('exampleData.csv', 'ab')
# for i in vert_np_array:
#     vert_np_array.savetxt(f, i, fmt='%i')






    # return data

# def save_image( npdata, outfilename ) :
#     img = Image.fromarray( np.asarray( np.clip(npdata,0,255), dtype="uint8"), "L" )
    # msc.imsave()
# save_image(load_image("/Users/nickdugal/desktop/pics/vertical/vertical600.png"),"outputtest.csv")
# ds = SupervisedDataSet(2,1)

# DS = ClassificationDataSet(inputdim, nb_classes=2, class_labels=['Fish','Chips'])
# image = Image.open("/Users/nickdugal/desktop/pics/vertical/vertical600.png")


# face = misc.imread("/Users/nickdugal/desktop/pics/vertical/vertical600.png")
# type(face)

#face.shape, face.dtype
# print(face[:])
# img = load_image("/Users/nickdugal/desktop/pics/vertical/vertical600.png")
# myfile = open('imagesArray.csv', 'r')
# wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
# wr.writerow(pack('i',img))

# with open('imagesArray.csv', 'wb') as myfile:
#     wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#     wr.writerow(np.array(face[:]))