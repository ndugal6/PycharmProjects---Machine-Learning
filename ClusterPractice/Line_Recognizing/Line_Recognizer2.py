from scipy import misc
import operator
import matplotlib.pyplot as plt
#Making a frequency chart of the 10,000 pixels when flattened(combining the colors into single grayscale layer), versus setting mode='L' (black and white) showed a difference
#Flatten returns floating point values allowing increased accuracy while  black&white used int
#If Not deleted/Open freq_modeL & flatten
#Used on oscilating/wave1.jpeg
imPixels = misc.imread("/Users/nickdugal/desktop/pics/oscilating/wave1.jpeg", flatten=True)
# imPixels = misc.imread("/Users/nickdugal/desktop/pics/oscilating/wave1.jpeg", mode='L')
num_frequency = {}

for i in imPixels:
    for num in i:
        # for num in j:
        if num in num_frequency:
                num_frequency[num] += 1
        else:
                num_frequency[num] = 1

file = open('freq_modeFlatten.txt','w')
file2 = open('freq_modeL.txt','w')




#itemgetter(0) sorts by number, itemgetter(1) sorts by frequency
for key, value in reversed(sorted(num_frequency.items(), key=operator.itemgetter(1))):
    file.write('{:<20}, {:<10}\n'.format(key, value))


