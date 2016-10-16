# charset = utf-8

from datetime import datetime as dt

start = dt.now()

# The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
# There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
# How many circular primes are there below one million?

def isprime(a):
    for x in xrange(3,int(a**0.5)+1,2):
        if a%x == 0:
            return 0
    return 1

prime = [2,3,5,7]
notlist = ['0','2','4','6','8']

for x in xrange(9,1000000,2):
    # if any number has 0,2,4,6,8 then ignore
    temp = str(x)
    if not(any(y in temp for y in notlist)):
        if isprime(x):
            prime.append(x)

maxcount = 4
for x in xrange(4,len(prime),1):
# for x in xrange(50,51,1):
    temp = str(prime[x])
    count = 0
    loopcount = len(temp)
    for y in xrange(0,loopcount,1):
        if int(temp) in prime:
            count += 1
            # print count
        # Rotate temp
        # print temp
        temp1 = temp[0]
        temp = str(int(temp)%(10**(loopcount-1)))
        temp = temp+temp1
    if count == loopcount:
        # print temp
        maxcount += 1

print maxcount



print('Solution took: ' + str(dt.now()-start) + ' ms')
