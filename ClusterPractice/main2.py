from scipy import ndimage
from scipy import misc
import numpy as np



face = misc.face()
print(type(face))

#Creating numpy array from image file
line = misc.imread("/Users/nickdugal/desktop/pics/vertical/vertical1.jpeg")
print(type(line))
print(line.shape, line.dtype)

#Creating raw file
line.tofile('line.raw') #Create raw file
line_from_raw = np.fromfile('line.raw',dtype=np.uint8)
print(line_from_raw.shape)
line_from_raw.shape = (100, 100, 4)
print(line_from_raw.shape)

#memory mapping
line_memmap = np.memmap('line.raw', dtype=np.uint8,shape=(100,100,4))

for i in range(10):
    im = np.random.random_integers(0, 255, 10000).reshape((100, 100))
    misc.imsave('random_%02d.png' % i, im)
from glob import glob
filelist = glob('random*.png')
filelist.sort()

###################More attempts IDK MAYBE USEFUL TO LOOK AT




#x = np.empty([60000, 60000])

x = np.zeros((10000,4))
y = []
for i in range(20):
    n = misc.imread("/Users/nickdugal/desktop/pics/oscilating/wave" + str(1) + ".jpeg") / 255
    w, h, d = original_shape = tuple(n.shape)
    image_array = np.reshape(n, (w * h, d))
    #print(image_array.shape)
    x = np.concatenate((x,image_array), axis=0)
    y.append(0)
dataset = dict(data = x, target = y)
print(type(dataset))



china = misc.imread("/Users/nickdugal/desktop/pics/oscilating/wave1.jpeg") / 255
print(type(china))
# Load Image and transform to a 2D numpy array.
w, h, d = original_shape = tuple(china.shape)
assert d == 4, print(china.shape)
print(china.shape)
image_array = np.reshape(china, (w * h, d))
#for i in china[[][0:]]: