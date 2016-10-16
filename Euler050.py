# coding=utf-8

from datetime import datetime

start = datetime.now()

# The prime 41, can be written as the sum of six consecutive primes:
# 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?

def isprime(a):
    for x in xrange(3,int(a**0.5)+1,2):
        if a%x == 0:
            return 0
    return 1

primelist = [2,3,5,7]

for i in xrange(11,1000000,2):
    if isprime(i):
        primelist.append(i)

# print primelist

start = 0
curr = 1
temp = primelist[start]
maxz = 0
maxstart = 0
maxcurr = 1
maxtemp = primelist[start]

upper = max(primelist)

i = 0

while i <= (len(primelist)-maxcurr):
    j = i
    while j < len(primelist):
        if sum(primelist[i:j]) > upper:
            break
        elif (j-i) > maxz:
            if sum(primelist[i:j]) in primelist:
                if maxcurr < (j-i):
                    maxz = j-i
                    maxstart = i
                    maxcurr = j
                    maxtemp = sum(primelist[i:j])
        j = j+1
    i = i+1




print maxtemp, maxz, maxstart, maxcurr






# print('Solution took: ' + str(datetime.now()-start) + ' ms')
