# coding = UTF-8

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

from datetime import datetime

start = datetime.now()

def isprime(a):
    for x in xrange(3,int(a**0.5)+1,1):
        if a%x == 0:
            return 0
    return 1

sum = 17

prime = 9

while prime<2000000:
    if isprime(prime):
        sum+=prime
    prime +=2

print sum

print('Solution took: ' + str(datetime.now()-start))
