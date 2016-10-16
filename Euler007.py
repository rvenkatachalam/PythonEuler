# coding = UTF-8

# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?

def isprime(a):
    for x in xrange(3, int(a**0.5)+1, 1):
        if a%x == 0:
            return 0
    return 1

now = 11

for x in xrange(5,10002,1):
    while isprime(now) == 0:
        now+=2
    now+=2

print x, now-2
