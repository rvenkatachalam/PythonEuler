# coding=utf-8

from datetime import datetime as dt

start = dt.now()

# A positive fraction whose numerator is less than its denominator is called a proper fraction.
# For any denominator, d, there will be d−1 proper fractions; for example, with d = 12:
# 1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12 .
# We shall call a fraction that cannot be cancelled down a resilient fraction.
# Furthermore we shall define the resilience of a denominator, R(d), to be the ratio of its proper fractions that are resilient; for example, R(12) = 4/11 .
# In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10 .
# Find the smallest denominator d, having a resilience R(d) < 15499/94744 .

prime = [1,2,3,5]
nonmult = []

s = 1

def isprime(a):
    for i in xrange(3,int(a**0.5)+1,2):
        if a%i == 0:
            return 0
    prime.append(a)
    return 1

x = 1*2*3*5*7*11*13

for i in xrange(1,x,1):
    if i%2 == 0 or i%3 == 0 or i%5 == 0 or i%7 ==0 or i%11 == 0 or i%13 ==0:
        s = s
    else:
        s = s+1
        nonmult.append(i)
        if i>1:
            isprime(i)



# print prime[46:66]
# print nonmult[42:62]
# print len(prime[6:]), len(nonmult[1:])
# # We need to find a number > 94766 where number of factors resilent is less than 15499

x1 = [nonmult[i] for i in xrange(0,len(nonmult),1) if nonmult[i] in prime]
# Prime numbers that are appearing as non multiples
print x1
print len(x1)



print x,len(nonmult), 1.0*len(nonmult)/x
# print prime




print('Solution took: ' + str((dt.now()-start).total_seconds()))
