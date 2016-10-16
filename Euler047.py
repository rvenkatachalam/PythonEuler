# coding=utf-8

from datetime import datetime

start = datetime.now()

# The first two consecutive numbers to have two distinct prime factors are:
# 14 = 2 × 7
# 15 = 3 × 5
# The first three consecutive numbers to have three distinct prime factors are:
# 644 = 2² × 7 × 23
# 645 = 3 × 5 × 43
# 646 = 2 × 17 × 19.
# Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?

prime = [2,3,5,7]
primefactnum = []

def isprime(a):
    for x in xrange(2,int(a**0.5),1):
        if a%x == 0:
            return 0
    return 1


s = 8
success = 0
fact = 4 #change to 4

def isprimefactnum(a):
    s = 0
    rem = a
    further = 1
    factors = []
    while further == 1:
        if rem%prime[s] == 0:
            rem = rem/prime[s]
            if prime[s] not in factors:
                factors.append(prime[s])
        elif rem/prime[s] < 1:
            further = 0
        else:
            s += 1
    factors = sorted(set(factors))
    if len(factors) == fact:
        primefactnum.append(a)
        return 1
    return 0


def cons(a):
    l = len(primefactnum) - 1
    if primefactnum[l] == a:
        if primefactnum[l-1] == a-1:
            if primefactnum[l-2] == a-2:
                if primefactnum[l-3] == a-3:
                    return 1

while success == 0:
    if isprime(s):
        prime.append(s)
    else:
        if isprimefactnum(s):
            if cons(s):
                success = 1
    s += 1

print max(primefactnum)-3

print('Solution took: ' + str((datetime.now()-start).total_seconds()) + ' seconds')
