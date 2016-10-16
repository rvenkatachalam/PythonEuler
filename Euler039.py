# encoding=utf-8

from datetime import datetime as dt

start = dt.now()

# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.
# {20,48,52}, {24,45,51}, {30,40,50}
# For which value of p ≤ 1000, is the number of solutions maximised?


maxx = 0
maxcount = 0

for x in xrange(1000,10,-1):
    count = 0
    for a in xrange(x-3,int(x/3)-1,-1):
        for b in xrange(1,int(a*2/3)+1,1):
            c = x - a - b
            if a**2 == (b**2 + c**2):
                # print a,b,c
                count += 1
    if count>maxcount:
        maxx = x
        maxcount = count

print maxx, maxcount

print('Solution took: ' + str(dt.now()-start) + ' ms')
