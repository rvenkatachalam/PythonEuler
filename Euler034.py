# coding=utf-8

# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
# Note: as 1! = 1 and 2! = 2 are not sums they are not included

from datetime import datetime
from math import factorial

start = datetime.now()

# print factorial(9)*7, len(str(factorial(9)*7))

max = 999999

test = 145

print sum(x for x in xrange(10,max,1) if sum(factorial(int(str(x)[y])) for y in xrange(0,len(str(x)),1)) == x)

print('Solution took: ' + str(datetime.now() - start) + ' ms')
