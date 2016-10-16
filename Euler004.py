# coding=utf-8
# A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

from datetime import datetime

start = datetime.now()

def reverse(a):
    b = str(a)
    y = ''
    for x in xrange(len(b)-1,-1,-1):
        y += b[x]
    if str(a) == y:
        return 1
    else:
        return 0

palin = []

for x in xrange(10000,1000001,1):
    if reverse(x):
        palin.append(x)

exit = 0

for x in xrange(len(palin)-1,-1,-1):
    y = palin[x]
    for z in xrange(100,1000,1):
        if (y%z == 0) and y/z in xrange(100,1000):
            print y, z, y/z
            exit = 1
            break
        if exit == 1:
            break
    if exit == 1:
        break

print datetime.now()-start
