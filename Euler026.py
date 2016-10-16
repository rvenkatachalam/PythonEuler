# coding=utf-8

# A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

# 1/2	= 	0.5
# 1/3	= 	0.(3)
# 1/4	= 	0.25
# 1/5	= 	0.2
# 1/6	= 	0.1(6)
# 1/7	= 	0.(142857)
# 1/8	= 	0.125
# 1/9	= 	0.(1)
# 1/10	= 	0.1
# Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

from datetime import datetime

start = datetime.now()

def traverse(a):
    x = []
    seed = 1
    rem = seed%a
    length = 1
    if rem <> 0:
        while rem not in x and rem <> 0:
             x.append(rem)
             rem *= 10
             rem = rem%a
             length += 1
        # print x
        # print rem
        if rem <> 0:
            return len(x)-x.index(rem)
        else:
            return 0
    else:
        return 0

mv = 0
d = 0

for x in xrange(1,1000,1):
    y = traverse(x)
    if y > mv:
        mv = y
        d = x

print d

print('Solution took: ' + str(datetime.now() - start) + ' ms')
