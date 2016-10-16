# coding=utf-8

# A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
#
# A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
#
# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
#
# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from datetime import datetime

start = datetime.now()

ab = []

def factors(n):
    a = set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    a.remove(max(a))
    return a

for x in xrange(2,28124,1):
    if sum(factors(x)) > x:
        ab.append(x)

# print ab

sumab = []

for x in xrange(0,len(ab),1):
    for y in xrange(x,len(ab),1):
        sumab.append(ab[x]+ab[y])

sumab = set(sumab)

finalsum = 0

for x in xrange(1,28124,1):
    if x not in sumab:
        finalsum += x

print finalsum

# print sumab

# print factors(28112)
# print sum(factors(28112))

print('Solution took: ' + str(datetime.now()-start))
