# coding = utf-8

# A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.
# Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?

from datetime import datetime

start = datetime.now()

m = 0

for i in xrange(2,100):
    for j in xrange(2,100):
        y = i ** j
        if m <  sum(int(str(y)[x]) for x in xrange(0,len(str(y)),1)):
            m = sum(int(str(y)[x]) for x in xrange(0,len(str(y)),1))

print m

# y = 1234
#
# print sum(int(str(y)[x]) for x in xrange(len(str(y))))

print('Solution took: ' + str(datetime.now()-start) + ' ms')
