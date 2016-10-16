# coding=utf-8

from datetime import datetime as dt

start = dt.now()

# Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.
# 37 36 35 34 33 32 31
# 38 17 16 15 14 13 30
# 39 18  5  4  3 12 29
# 40 19  6  1  2 11 28
# 41 20  7  8  9 10 27
# 42 21 22 23 24 25 26
# 43 44 45 46 47 48 49
# It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.
# If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

def isprime(a):
    for i in xrange(2,int(a**0.5),1):
        if a%i == 0:
            return 0
    return 1

count = 8.0
i = 7

while count/(i*2-1) >= 0.1:
    i += 2
    cor = i*i
    cor = cor -i + 1
    if isprime(cor):
        count += 1
    cor = cor -i + 1
    if isprime(cor):
        count += 1
    cor = cor -i + 1
    if isprime(cor):
        count += 1

print i

print('Solution took: ' + str((dt.now()-start).total_seconds()) + ' seconds')
