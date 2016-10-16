# coding=utf-8

# The series, 11 + 22 + 33 + ... + 1010 = 10405071317.
#
# Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

from datetime import datetime

start = datetime.now()

print(sum((x**x)%10000000000 for x in xrange(1,1001,1)))

print('Solution took: ' + str(datetime.now()- start) + ' ms')
