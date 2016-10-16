# coding = UTF-8

# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a2 + b2 = c2
# For example, 32 + 42 = 9 + 16 = 25 = 52.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

from datetime import datetime

start = datetime.now()

squarenumber = []

for x in xrange(1,1001,1):
    squarenumber.append(x**2)

squarenumber = sorted(squarenumber, reverse=0)
a = b = c = 0
for x in xrange(999,2,-1):
    for y in xrange(x-1,0,-1):
        if (squarenumber[x]-squarenumber[y]) in squarenumber[0:999]:
            if (squarenumber[x]**0.5 + squarenumber[y]**0.5 + (squarenumber[x] - squarenumber[y])**0.5) == 1000:
                print (squarenumber[x]**0.5) * (squarenumber[y]**0.5) * (squarenumber[x] - squarenumber[y])**0.5
                y=-1
                x=-1

print ('Solution took: ' + str(datetime.now()-start))
