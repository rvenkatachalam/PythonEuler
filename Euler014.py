# coding=utf-8

# The following iterative sequence is defined for the set of positive integers:
#
# n → n/2 (n is even)
# n → 3n + 1 (n is odd)
#
# Using the rule above and starting with 13, we generate the following sequence:
#
# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.
#
# Which starting number, under one million, produces the longest chain?
#
# NOTE: Once the chain starts the terms are allowed to go above one million.

from datetime import datetime

start = datetime.now()

d = {1:1, 2:2}

def link(a):
    c = 1
    while a <> 1:
        if d.has_key(a):
            # print('Step haskey found and count is ' + str(c))
            c += d[a]
            a = 1
        elif a%2 == 0:
            a = a/2
            c += 1
            # print('Step even number and number and count is '+ str(a) + '....' + str(c))
        elif a <> 1:
            a = 3*a + 1
            c += 1
            # print('Step odd number and number and count is '+ str(a) + '....' + str(c))
    return c-1

for x in xrange(3,1000000,1):
    d[x] = link(x)

y = max(d.values())
print y
print d.keys()[d.values().index(y)]

#
#
#
# print max(d.values())
#
# if d.has_key(7):
#     print d[7]
# else:
#     print('Error111')
#
# print d.keys()[d.values().index(10)]

print('Solution took: ' + str(datetime.now()-start))
