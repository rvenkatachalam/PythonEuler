# coding=utf-8

# Concealed Square
# Problem 206
# Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
# where each “_” is a single digit.

from datetime import datetime

start = datetime.now()

min = int(10203040506070809**0.5) + 1
max = int(19293949596979899**0.5) + 1

y = []

for x in xrange(min, max, 1):
    if x%10 in (3,7):
        z = x**2
        if int(z/100)%10 == 8:
            if int(z/10000)%10 == 7:
                if int(z/1000000)%10 == 6:
                    if int(z/100000000)%10 == 5:
                        if int(z/10000000000)%10 == 4:
                            if int(z/1000000000000)%10 == 3:
                                if int(z/100000000000000)%10 == 2:
                                    y.append(x)

print len(y)
print y


print('Solution took: ' + str(datetime.now()-start) + ' ms')
