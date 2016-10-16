# coding=utf-8

from datetime import datetime as dt
from math import factorial

start = dt.now()

# There are exactly ten ways of selecting three from five, 12345:
# 123, 124, 125, 134, 135, 145, 234, 235, 245, and 345
# In combinatorics, we use the notation, 5C3 = 10.
# In general,
# nCr =
# n!
# r!(n−r)!
# ,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
# It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.
# How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?

def ncr(a,b):
    return factorial(a)/factorial(b)/factorial(a-b)

count = 0

for x in xrange(1,101,1):
    for y in xrange(0,x,1):
        if ncr(x,y) > 1000000:
            count += 1

print count


print('Solution start: ' + str(start) + '\nSolution end  : ' + str(dt.now()))
