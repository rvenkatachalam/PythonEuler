# coding=utf-8

# What is most surprising is that the important mathematical constant,
# e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

from datetime import datetime
start = datetime.now()

pot = [2,1,2,1]

for x in xrange(0,33,1):
    pot.append(1)
    pot.append(pot[len(pot)-3]+2)
    pot.append(1)

x = 99
num = pot[x-1]
den = pot[x]
num = num * den + 1
num, den = den, num
print pot[x], num, den

for x in xrange(98,0,-1):
    num = num + pot[x-1]*den
    num, den = den, num
    for i in xrange(2,101,1):
        while num%i==0 and den%i==0:
            num = num/i
            den = den/i
    print pot[x], num, den


print den


print sum(list(int(str(num)[i]) for i in range(len(str(num)))))
print sum(list(int(str(den)[i]) for i in range(len(str(den)))))






print('Solution took: ' + str(datetime.now()-start) + ' ms')
