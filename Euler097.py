# coding=utf-8

from datetime import datetime as dt

start = dt.now()

# The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 26972593−1; it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2p−1, have been found which contain more digits.
# However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×27830457+1.
# Find the last ten digits of this prime number.

s = 28433
i = 2

for x in xrange(1,7830457,1):
    i = i * 2
    i = i % 100000000000

i = (i * s)%100000000000 + 1

print i


# print rep

print('Solution took: ' + str((dt.now()-start).total_seconds()) + ' seconds')
