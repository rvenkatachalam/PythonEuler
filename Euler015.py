# coding=utf-8

# Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
# How many such routes are there through a 20×20 grid?

from datetime import datetime
import numpy

start = datetime.now()

mat = numpy.empty([21,21])

for x in xrange(0,21,1):
    for y in xrange(0,21,1):
        if x == 0:
            mat[x][y] = 1
        elif y == 0:
            mat[x][y] = 1
        else:
            mat[x][y] = mat[x][y-1] + mat[x-1][y]

print mat[20][20]

print('Solution took: ' + str(datetime.now()-start) + ' ms')
