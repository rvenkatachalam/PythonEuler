# coding=utf-8

from datetime import datetime as dt

start = dt.now()

# A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.
# The text file, keylog.txt, contains fifty successful login attempts.
# Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.

txt = open('euler079.txt').read()

num = []
temp = ''

for i in xrange(0,len(txt),1):
    if ord(txt[i]) in range(48,58):
        temp += txt[i]
    else:
        num.append(temp)
        temp = ''

base = []

for x in xrange(0,len(num),1):
    for y in xrange(0,len(num[x]),1):
        base.append(num[x][y])

base = sorted(set(base))

final = base

for i in xrange(0,len(base),1):
    base = sorted(set(base))
    temp = base[0]
    for j in xrange(0,len(num),1):
        if temp in num[j]:
            if temp in num[j][1:]:
                temp = num[j][0]
    final[i] = temp
    for j in xrange(0,len(num),1):
        t = [num[j][k] for k in xrange(0,len(num[j]),1)]
        if temp in t:
            t.remove(temp)
        t1 = ''.join(t[x] for x in xrange(0,len(t),1))
        num[j] = t1
    base.remove(temp)

print ''.join(final[x] for x in xrange(0,len(final),1))

print('Solution took: ' + str((dt.now()-start).total_seconds()) + ' seconds')
