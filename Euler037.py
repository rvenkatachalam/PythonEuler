# encoding=utf-8

from datetime import datetime as dt

start = dt.now()

# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

def isprime(a):
    for x in xrange(3,int(a**0.5)+1,2):
        if a%x == 0:
            return 0
    return 1

prime = [2,3,5,7]
ends = [3,7]
mids = [1,3,7,9]
trunc = []
count = 0

def checktrunc(a):
    count = 0
    for x in xrange(0,len(str(a)),1):
        if isprime(int(str(a)[x:])) and isprime(int(str(a)[:(len(str(a))-x)])):
            count += 1
    if count == len(str(a)):
        trunc.append(a)


for x in xrange(0,len(prime),1):
    for y in xrange(0,len(ends),1):
        temp = int(str(prime[x]) + str(ends[y]))
        checktrunc(temp)

nextstart = 0
count = len(trunc)

while count<11:
    for x in xrange(0,len(prime),1):
        for y in xrange(0,len(ends),1):
            for z in xrange(nextstart,len(mids),1):
                temp = int(str(prime[x]) + str(mids[z]) + str(ends[y]))
                checktrunc(temp)
    temp = nextstart
    nextstart = len(mids)
    for x in xrange(temp,nextstart,1):
        mids.append(int(str(mids[x]) + '1'))
        mids.append(int(str(mids[x]) + '3'))
        mids.append(int(str(mids[x]) + '7'))
        mids.append(int(str(mids[x]) + '9'))
    count = len(trunc)

print trunc
print sum(trunc)

print('Solution took: ' + str(dt.now()-start) + ' ms')
