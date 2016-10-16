# coding=utf-8

# In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
# It is possible to make £2 in the following way:
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

from datetime import datetime

start = datetime.now()

count = 1
loopcount = 0

for p100 in xrange(0,3,1):
    for p50 in xrange(0,5-p100,1):
        for p20 in xrange(0,11-int(p100*5+p50*2.5),1):
            for p10 in xrange(0,21-int(p100*10+p50*5+p20*2),1):
                for p05 in xrange(0,41-int(p100*20+p50*10+p20*4+p10*2),1):
                    for p02 in xrange(0,101-int(p100*50+p50*25+p20*10+p10*5+p05*2.5),1):
                        for p01 in xrange(0,201-int(p100*100+p50*50+p20*20+p10*10+p05*5+p02*2),1):
                            loopcount += 1
                            if (p100*100 + p50*50 + p20*20 + p10*10 + p05*5 + p02*2 + p01*1) == 200:
                                count += 1


print loopcount, count
# print loopcount, count

# 1.28 billion loops when you brute force
# Takes about _____ seconds

print('Solution took: ' + str(datetime.now()-start) + ' ms')
