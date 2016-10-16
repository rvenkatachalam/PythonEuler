# coding=UTF-8
#
# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

from datetime import datetime

start = datetime.now()

sum = 0
sum2 = 0

for x in xrange(1,101,1):
    sum += x
    sum2 += x**2

sum = sum**2


print sum - sum2
print('Time taken: '+ str(datetime.now()-start))
