# coding=utf-8

from datetime import datetime as dt

start = dt.now()

# The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.
# How many n-digit positive integers exist which are also an nth power?

cand = [1,2,3,4,5,6,7,8,9]

success = 0
seed = 10

while success == 0:
    base = seed**(1.0/(len(str(seed))))
    if int(base)-base <> 0:
        base = base + 1
    base = int(base)
    c = 0
    while len(str(base**len(str(seed)))) == len(str(seed)):
        cand.append(base**len(str(seed)))
        base += 1
        c = c + 1
    seed = seed * 10
    if c == 0:
        success = 1

print len(cand)


print('Solution took: ' + str((dt.now()-start).total_seconds()) + ' seconds')
