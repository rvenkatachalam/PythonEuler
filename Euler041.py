# coding=utf-8

from datetime import datetime as dt

start = dt.now()

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.
# What is the largest n-digit pandigital prime that exists?

from itertools import permutations as pm

perm = []

for x in xrange(9,3,-1):
    perm.append(list(pm([1,2,3,4,5,6,7,8,9],x)))

# print perm
perm1 = []

# print len(perm), len(perm[5])


for x in xrange(0,len(perm),1):
    for y in xrange(0,len(perm[x]),1):
        if perm[x][y][len(perm[x][y])-1] not in [0,2,4,5,6,8]:
            temp = ''
            for i in xrange(0,len(perm[x][y]),1):
                temp += str(perm[x][y][i])
            perm1.append(int(temp))

perm1 = sorted(set(perm1))

def isprime(a):
    for x in xrange(3,int(a**0.5)+1,2):
        if a%x == 0:
            return 0
    return 1

success = 0
start = len(perm1)-1

def pandigi(a):
    stra = [str(x) for x in xrange(1,len(str(a))+1,1)]
    strrip = []
    for x in xrange(0,len(str(a)),1):
        strrip.append(str(a)[x])
    strrip = sorted(strrip)
    if stra == strrip:
        return 1



while success == 0:
    if isprime(perm1[start]):
        if pandigi(perm1[start]):
            print perm1[start]
            success = 1
    start -= 1

print('Solution took: ' + str(dt.now()-start) + ' ms')
