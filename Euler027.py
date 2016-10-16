# coding=utf-8

# https://projecteuler.net/problem=27

from datetime import datetime

start = datetime.now()

# Assuming prime can only be positive numbers

def isprime(a):
    if a < 0:
        return 0
    y = int(a**0.5)+1
    for x in xrange(3,y,2):
        if a%x == 0:
            return 0
    return 1

# a = -74
# b = 971
#
# seed = 0
# checkprime = seed**2+a*seed+b
# while isprime(checkprime):
#     print seed, checkprime
#     seed += 1
#     checkprime = seed**2+a*seed+b



prime = [2,3,5,7]

for x in xrange(9,1000,2):
    if isprime(x):
        prime.append(x)

print prime
print len(prime)

#
# for x in xrange(0,len(prime),1):
#     prime.append(-1*prime[x])
#
# prime = sorted(prime)
#
maxchain = 0
maxa = 0
maxb = 0

looplen = len(prime)

for j in xrange(0,looplen,1):
    b = prime[j]
    for i in xrange(-999,1000,1):
        chain = 0
        a = i
        seed = 0
        checkprime = seed**2 + a*seed + b
        while isprime(checkprime):
            chain += 1
            seed += 1
            checkprime = seed**2 + a*seed + b
        if chain > maxchain:
            maxchain = chain
            maxa = a
            maxb = b


print maxchain, maxa, maxb, maxa*maxb
print len(prime)

print('Solution took: ' + str(datetime.now()-start) + ' ms')
