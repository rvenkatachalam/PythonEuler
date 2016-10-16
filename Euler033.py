# coding=utf-8

from datetime import datetime as dt

start = dt.now()

# The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.
# We shall consider fractions like, 30/50 = 3/5, to be trivial examples.
# There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.
# If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

fracnum = []
fracden = []

for x in xrange(11,90,1):
    for y in xrange(int(x/10)*10+10,100,1):
        if (x%10 <> 0) and (y%10 <> 0):
            tempx = '1'
            tempy = '1'
            if str(x)[0] == str(y)[1]:
                tempx = str(x)[1]
                tempy = str(y)[0]
            elif str(x)[1] == str(y)[0]:
                tempx = str(x)[0]
                tempy = str(y)[1]
            elif str(x)[1] == str(y)[1]:
                tempx = str(x)[0]
                tempy = str(y)[0]
            if (x*1.0/y) == (int(tempx)*1.0/int(tempy)):
                # print(x/y)
                fracnum.append(int(tempx))
                fracden.append(int(tempy))

num = 1
den = 1
for x in xrange(0,len(fracnum),1):
    num *= fracnum[x]
    den *= fracden[x]

print num, den



print('Solution took: ' + str(dt.now()-start) + ' ms')
