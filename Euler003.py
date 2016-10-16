# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

from datetime import datetime

time = datetime.now()
def isprime(a):
    for x in xrange(2,int(a**0.5)+1,1):
        if a%x == 0:
            return 0
    return 1

y = int(600851475143**0.5)+1
largeprime = 0

for x in xrange(1,y,1):
    if (600851475143%x==0):
        if isprime(x):
            largeprime = x

print largeprime
print('solution took: ' + str(datetime.now()-time))
