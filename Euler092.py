# coding=utf-8

from datetime import datetime as dt

start = dt.now()

# A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.
# For example,
# 44 → 32 → 13 → 10 → 1 → 1
# 85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89
# Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.
# How many starting numbers below ten million will arrive at 89?

# create list of squares that make up 89

l = [89]
sq = [1]

def sos(a):
    return sum(int(str(a)[i])**2 for i in xrange(0,len(str(a)),1))

c89 = 0

for i in xrange(1,10000001,1):
    t = sos(i)
    if t not in sq:
        if t in l:
            c89 += 1
        else:
            temp = []
            temp.append(t)
            while t not in (89,1) and t not in sq and t not in l:
                t = sos(t)
            if t == 1 or t in sq:
                sq.extend(temp)
            else:
                l.extend(temp)
                c89 += 1

print c89


print('Solution took: ' + str((dt.now()-start).total_seconds()) + ' seconds')
