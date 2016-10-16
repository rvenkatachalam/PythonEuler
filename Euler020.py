# coding=utf-8

# n! means n × (n − 1) × ... × 3 × 2 × 1
# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.
# Find the sum of the digits in the number 100!

from datetime import datetime
from math import factorial

start = datetime.now()

x = str(factorial(100))

# print x

s = 0

for y in xrange(0,len(x),1):
    s += int(x[y])

print s

print('Solution took: ' + str((datetime.now()-start).microseconds) + ' ms')
