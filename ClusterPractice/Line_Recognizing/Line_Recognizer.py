from scipy import misc

imPixels = misc.imread("/Users/nickdugal/desktop/pics/oscilating/wave1.jpeg", mode='RGB') /255
# print(imPixels[0])
# print(imPixels[0][0])
# print(imPixels[0][0][0])
file = open('linedata','r+')
imPix2 = imPixels[[]]
print(imPix2.shape)
imPix3 = imPixels[[]]
print(imPix3.shape)
# imPixels.tofile(file, ",","%s")
jNotZero = 0;
jZero = 0;
iNotZero = 0;
iZero = 0;
kNotZero = 0;
kZero = 0;
for i in imPixels[:]:
    if (not 0) in i: iNotZero += 1
    else: iZero += 1
    # i.tofile(file, ",","%s")
    for j in i[:]:
        if (not 0) in j: jNotZero += 1
        else: jZero += 1
        for k in j[:]: pass
            # print(i)
            # print(k)
print("Zeros in i: {} \n Others: {} \n Zeros in j: {} \n others:{} \n".format(iNotZero, iZero, jNotZero, jZero))
print(imPixels.shape)