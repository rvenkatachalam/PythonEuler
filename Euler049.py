# coding=utf-8

from datetime import datetime as dt

start = dt.now()

# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, but there is one other 4-digit increasing sequence.
# What 12-digit number do you form by concatenating the three terms in this sequence?

def isprime(a):
    for x in xrange(3,int(a**0.5)+1,2):
        if a%x == 0:
            return 0
    return 1

prime = []

for x in xrange(1001,10000,2):
    if isprime(x):
        prime.append(x)

def issame(a,b):
    sa = sorted([int(str(a)[x]) for x in xrange(0,len(str(a)),1)])
    sb = sorted([int(str(b)[x]) for x in xrange(0,len(str(b)),1)])
    if sa == sb:
        return 1
    return 0

for x in xrange(0,len(prime)-2,1):
    for y in xrange(x+1,len(prime)-1,1):
        if issame(prime[x],prime[y]):
            if (2*prime[y]-prime[x]) in prime:
                if issame(2*prime[y]-prime[x],prime[y]):
                    print str(prime[x])+str(prime[y])+str(2*prime[y]-prime[x])

print('Solution start: ' + str(start) + '\nSolution end  : ' + str(dt.now()))
