# coding=utf-8

from datetime import datetime as dt

start = dt.now()

# It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.
# 9 = 7 + 2×12
# 15 = 7 + 2×22
# 21 = 3 + 2×32
# 25 = 7 + 2×32
# 27 = 19 + 2×22
# 33 = 31 + 2×12
# It turns out that the conjecture was false.
# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

success = 0

prime = [2,3,5,7]

def isprime(a):
    for j in xrange(3,int(a**0.5)+1,2):
        if a%j == 0:
            return 0
    return 1

i = 9

while success == 0:
    if isprime(i):
        prime.append(i)
    else:
        x = 0
        innersuccess = 0
        innerfail = 0
        loopend = 0
        while loopend == 0:
            temp = (i-prime[x])/2
            if ((temp - int(temp) == 0)):
                temp1 = temp**0.5
                if (temp1 - int(temp1)) == 0:
                    innersuccess += 1
            x += 1
            if x == (len(prime)):
                loopend = 1
        if innersuccess == 0:
            success = 1
            print i
    i += 2

print('\nSolution start time: ' + str(start) + '\nSolution end   time: ' + str(dt.now()))
