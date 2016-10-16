# coding=utf-8

# Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
# For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.
# What is the total of all the name scores in the file?

from datetime import datetime

start = datetime.now()

txt = open('euler22.txt').read()

s = []

x = 0

while x<len(txt):
    c = ''
    while ord(txt[x]) in range(65,91):
        c += txt[x]
        x += 1
    if c <> '':
        s.append(c)
    x+=1

s = sorted(s)

base = 0

for x in xrange(0, len(s), 1):
    temp = 0
    for y in xrange(0,len(s[x]),1):
        temp += (ord(s[x][y])-64)
    base += temp*(x+1)

print base

# for x in xrange(0, len(s),1):
#     print s[x]

# print ord('A'), ord('Z') 65 to 90 = A to Z

print('Solution took: ' + str((datetime.now()-start).microseconds) + ' ms')
