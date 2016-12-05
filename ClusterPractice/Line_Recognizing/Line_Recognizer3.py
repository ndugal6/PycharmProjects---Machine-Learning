from scipy import misc
import operator
import matplotlib.pyplot as plt

imPixels = misc.imread("/Users/nickdugal/desktop/pics/oscilating/wave1.jpeg", flatten=True)


maxes = []
maxes2 = []
for ind in range(100):
    maxes.append(0.0)
    maxes2.append(0.0)
past = 0.0
next = 0.0
count = 0
for i in imPixels:
    past = float(i[0])
    for idx, num in enumerate(i[1:-1]):
        next = float(i[idx+1])
        if past <= num and num >= next:
            maxes[count] += 1
        past = float(num)
    count = count + 1
print(maxes)
changes = 0
for o in maxes:
    if 98 - o != 0:
        changes += 1
print(changes)

# min = 0
# max = 0
# for count, cur in enumerate(maxes[1:-1]):
#     cur = int(cur)
#     if (maxes[count-1] > cur) and (maxes[count+1] > cur): min += 1;
#     if (maxes[count-1] < cur) and (maxes[count+1] < cur): max += 1;

theMax = 0
theMin = 0
for n in range(len(maxes)):
    if n == 0: continue
    if n == len(maxes) - 1:continue
    a,b,c = maxes[n-1], maxes[n], maxes[n+1]
    if b < a:
        if b < c:
            theMin = theMin + 1
    elif b > a:
        if b > c:
            theMax = theMax + 1

print('the max is' + str(theMax) + 'the min is: ' + str(theMin))
def fix_values(dollars):
    return dollars * 2

imPixels = misc.imread("/Users/nickdugal/desktop/pics/horizontal/horizontal1.jpeg", flatten=True)
maxes.clear()
for ind in range(100): maxes.append(0.0)
for j in imPixels:
    for n in range(len(maxes)):
        if n == 0.0: continue
        if n == len(maxes) - 1: continue
        a, b, c = maxes[n - 1], maxes[n], maxes[n + 1]
        if b < a:
            if b < c:
                theMin = theMin + 1
        elif b > a:
            if b > c:
                theMax = theMax + 1