# coding=utf-8

# You are given the following information, but you may prefer to do some research for yourself.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

from datetime import datetime

start = datetime.now()

s = 1
c = 0
cal = {1:31,2:28,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}

for x in xrange(1900,2001,1):
    for y in xrange(1,13,1):
        if s%7 == 0 and x<>1900:
            c += 1
            print('1-' + str(y) + '-'+str(x))
        s+=cal[y]
        if (x%4 == 0) and (y ==2) and (x%100<>0):
            s+=1
        if (x%400 == 0) and (y==2):
            s+=1
print c


print('Solution took: ' + str((datetime.now()-start).microseconds))
