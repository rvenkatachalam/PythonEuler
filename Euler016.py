# coding=utf-8

# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 21000?

from datetime import datetime

start = datetime.now()

x = str(2**1000)
s = 0
for y in xrange(0,len(x),1):
    s += int(x[y])

print s

print('Wolution took: '+ str(datetime.now()-start))
