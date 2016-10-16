# coding=utf-8

from datetime import datetime as dt

from itertools import permutations as pt

start = dt.now()

# Triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers are all figurate (polygonal) numbers and are generated by the following formulae:
#
# Triangle	 	P3,n=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Square	 	P4,n=n2	 	1, 4, 9, 16, 25, ...
# Pentagonal	 	P5,n=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
# Hexagonal	 	P6,n=n(2n−1)	 	1, 6, 15, 28, 45, ...
# Heptagonal	 	P7,n=n(5n−3)/2	 	1, 7, 18, 34, 55, ...
# Octagonal	 	P8,n=n(3n−2)	 	1, 8, 21, 40, 65, ...
# The ordered set of three 4-digit numbers: 8128, 2882, 8281, has three interesting properties.
#
# The set is cyclic, in that the last two digits of each number is the first two digits of the next number (including the last number with the first).
# Each polygonal type: triangle (P3,127=8128), square (P4,91=8281), and pentagonal (P5,44=2882), is represented by a different number in the set.
# This is the only set of 4-digit numbers with this property.
# Find the sum of the only ordered set of six cyclic 4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, is represented by a different number in the set.

tri = []
sq = []
pent = []
hex = []
hept = []
oct = []

tri1 = sq1 = pent1 = hex1 = hept1 = oct1 = 0
n = 1
while tri1 == 0:
    if tri1 == 0:
        t = n * (n+1) / 2
        if len(str(t)) == 4:
            tri.append(t)
        elif len(str(t)) > 4:
            tri1 = 1
    if sq1 == 0:
        t = n * n
        if len(str(t)) == 4:
            sq.append(t)
        elif len(str(t)) > 4:
            sq1 = 1
    if pent1 == 0:
        t = n * (3*n - 1) / 2
        if len(str(t)) == 4:
            pent.append(t)
        elif len(str(t)) > 4:
            pent1 = 1
    if hex1 == 0:
        t = n * (2*n - 1)
        if len(str(t)) == 4:
            hex.append(t)
        elif len(str(t)) > 4:
            hex1 = 1
    if hept1 == 0:
        t = n * (5*n - 3) / 2
        if len(str(t)) == 4:
            hept.append(t)
        elif len(str(t)) > 4:
            hept1 = 1
    if oct1 == 0:
        t = n * (3*n - 2)
        if len(str(t)) == 4:
            oct.append(t)
        elif len(str(t)) > 4:
            oct1 = 1
    n += 1




print x
print('Solution took: ' + str((dt.now()-start).total_seconds()) + ' seconds')