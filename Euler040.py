# coding=utf-8

from datetime import datetime as dt

start = dt.now()

# An irrational decimal fraction is created by concatenating the positive integers:
# 0.123456789101112131415161718192021...
# It can be seen that the 12th digit of the fractional part is 1.
# If dn represents the nth digit of the fractional part, find the value of the following expression.
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

d1 = d10 = d100 = d1000 = d10000 = d100000 = d1000000 = 0

counter = 0
seed = 1

while counter < 1000001:
    oldcounter = counter
    counter += len(str(seed))
    if oldcounter < 1 and counter >= 1:
        d1 = int(str(seed)[1-oldcounter-1])
    elif oldcounter < 10 and counter >= 10:
        d10 = int(str(seed)[10-oldcounter-1])
    elif oldcounter < 100 and counter >= 100:
        d100 = int(str(seed)[100-oldcounter-1])
    elif oldcounter < 1000 and counter >= 1000:
        d1000 = int(str(seed)[1000-oldcounter-1])
    elif oldcounter < 10000 and counter >= 10000:
        d10000 = int(str(seed)[10000-oldcounter-1])
    elif oldcounter < 100000 and counter >= 100000:
        d100000 = int(str(seed)[100000-oldcounter-1])
    elif oldcounter < 1000000 and counter >= 1000000:
        d1000000 = int(str(seed)[1000000-oldcounter-1])
    seed += 1

print d1 * d10 * d100 * d1000 * d10000 * d100000 * d1000000


print('Solution took: ' + str(dt.now()-start) + ' ms')
