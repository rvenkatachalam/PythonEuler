# coding=utf-8

# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

from datetime import datetime

start = datetime.now()

ami = {}

def amicable(x):
    s = 0
    # l = []
    for y in xrange(1, (x+2)/2, 1):
        if x%y == 0:
            s += y
            # l.append(y)
    ami[x] = s
    # print l

for x in xrange(1,10001,1):
    amicable(x)

pair = []

for x in xrange(2,10001,1):
    if ami[x] in ami:
        if ami[ami[x]] == x and ami[x] <> x:
            pair.append(x)

print pair
print sum(pair)
# for x in xrange(2,1001,2):


print('Solution took: ' + str((datetime.now() - start).microseconds) + ' ms')
