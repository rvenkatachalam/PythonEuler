# coding=utf-8

from datetime import datetime as dt

start = dt.now()

# Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
# Triangle	 	Tn=n(n+1)/2	 	1, 3, 6, 10, 15, ...
# Pentagonal	 	Pn=n(3n−1)/2	 	1, 5, 12, 22, 35, ...
# Hexagonal	 	Hn=n(2n−1)	 	1, 6, 15, 28, 45, ...
# It can be verified that T285 = P165 = H143 = 40755.
# Find the next triangle number that is also pentagonal and hexagonal.

tri = [1]
seedtri = [1,2]
pent = [1]
seedpent = [1,2]
hex = [1]
seedhex = 2
success = 1

def checktri(a):
    stri = max(seedtri)
    while max(tri) < a:
        tri.append(stri*(stri + 1) / 2)
        stri += 1
        seedtri.append(stri)
    if max(tri) == a:
        return 1

def checkpent(a):
    spent = max(seedpent)
    while max(pent) < a:
        pent.append(spent*(3*spent - 1) / 2)
        spent += 1
        seedpent.append(spent)
    if max(pent) == a:
        return 1

while success <= 40755:
    temp = seedhex*(2*seedhex-1)
    hex.append(temp)
    if checktri(temp) and checkpent(temp):
        success = temp
    seedhex += 1
    # print tri, pent, hex

print tri
print pent
print hex
print success


print('Solution took: ' + str(dt.now()-start) + ' ms')
