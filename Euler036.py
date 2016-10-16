# coding=utf-8

# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, in either base, may not include leading zeros.)

from datetime import datetime

start = datetime.now()

palin = list(num for num in xrange(1,1000001,1) if (sum(1 if str(num)[x] == str(num)[len(str(num))-x-1] else 0 for x in xrange(0,len(str(num))/2,1)) == int(len(str(num))/2)))

def ispalin(num):
    s = bin(num)[2:]
    return (1 if (sum(1 if str(s)[x] == str(s)[len(str(s))-x-1] else 0 for x in xrange(0,len(str(s))/2,1)) == int(len(str(s))/2)) else 0)

print sum(palin[x] for x in xrange(0,len(palin)) if ispalin(palin[x]) == 1)

print('Solution took: ' + str(datetime.now()-start) + ' ms')
