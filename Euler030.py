# coding=utf-8

# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 14 + 64 + 34 + 44
# 8208 = 84 + 24 + 04 + 84
# 9474 = 94 + 44 + 74 + 44
# As 1 = 14 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

from datetime import datetime

start = datetime.now()

n = 9

def pow5(a):
    s = 0
    for x in xrange(0,len(str(a)),1):
        s += int(str(a)[x])**5
    return s

while len(str(n)) < len(str(pow5(n))):
    n = int(str(n) + '9')

print n

print(sum(x for x in xrange(10,n) if pow5(x) == x))

print('Solution took: ' + str(datetime.now() - start) + ' ms')
