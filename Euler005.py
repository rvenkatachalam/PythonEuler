# coding=UTF-8
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
# Write HCF algorithm and multiple

from datetime import datetime

start = datetime.now()

y = range(1,21)
prod = 1
print y

x = 2
exit = 0

while exit==0:
    atleast = 0
    for z in xrange(0,len(y),1):
        if y[z]%x == 0:
            atleast = 1
            y[z] = y[z]/x
    if atleast == 1:
        prod *= x
        print x,prod,y
    else:
        if sum(y) == 20:
            exit = 1
        else:
            x +=1


print prod
print y
print exit
print('Solution took:' + str(datetime.now()-start))
