# coding = utf-8

from datetime import datetime as dt

start = dt.now()

# It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.
# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

def issame(a,b):
    stra = [str(a)[x] for x in xrange(0,len(str(a)),1)]
    strb = [str(b)[x] for x in xrange(0,len(str(b)),1)]
    if sorted(stra) == sorted(strb):
        return 1

seed = 11

success = 0

while success == 0:
    if issame(seed,seed*2):
        if issame(seed, seed*3):
            if issame(seed, seed*4):
                if issame(seed, seed*5):
                    if issame(seed, seed*6):
                        print seed, seed*2, seed*3, seed*4, seed*5, seed*6
                        success = 1
    seed += 1

print('Solution took: ' + str(dt.now()-start) + ' ms')
