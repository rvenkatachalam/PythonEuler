# coding=utf-8

from datetime import datetime as dt 

start = dt.now() 

# The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.
# Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:
# d2d3d4=406 is divisible by 2
# d3d4d5=063 is divisible by 3
# d4d5d6=635 is divisible by 5
# d5d6d7=357 is divisible by 7
# d6d7d8=572 is divisible by 11
# d7d8d9=728 is divisible by 13
# d8d9d10=289 is divisible by 17
# Find the sum of all 0 to 9 pandigital numbers with this property.

from itertools import permutations as pm 

lst = [1,2,3,4,5,6,7,8,9,0]

poss = []
poss17 = []

poss = list(pm(lst,3))


for x in xrange(0,len(poss),1): 
	temp = (''.join(str(poss[x][y]) for y in xrange(0,len(poss[x]),1)))
	if int(temp)%17 == 0: 
		poss17.append(poss[x])

poss13 = []

for x in xrange(0,len(poss17),1): 
	newlst = list(lst[y] for y in xrange(0,len(lst),1) if lst[y] not in poss17[x]) 
	for i in xrange(0,len(newlst),1): 
		tempstr = list(list(str(newlst[i])[0]) + list(poss17[x]))
		temp = int(str(tempstr[0]) + str(tempstr[1]) + str(tempstr[2]))
		if temp%13 == 0: 
			ttemp = ''
			for j in xrange(0,4,1): 
				ttemp += str(tempstr[j])
			poss13.append(ttemp)
	

poss11 = []

for x in xrange(0,len(poss13),1): 
	newlst = []
	templst = []
	for i in range(len(str(poss13[x]))): 
		templst.append(int(str(poss13[x])[i]))
	newlst = list(lst[y] for y in xrange(0,len(lst),1) if lst[y] not in templst)
	for i in xrange(0,len(newlst),1):
		temp = str(newlst[i]) + poss13[x]
		if int(temp[:3])%11 == 0: 
			poss11.append(temp)

poss7 = [] 

for x in xrange(0,len(poss11),1): 
	newlst = []
	templst = []
	for i in range(len(str(poss11[x]))): 
		templst.append(int(str(poss11[x])[i]))
	newlst = list(lst[y] for y in xrange(0,len(lst),1) if lst[y] not in templst)
	for i in xrange(0,len(newlst),1):
		temp = str(newlst[i]) + poss11[x]
		if int(temp[:3])%7 == 0: 
			poss7.append(temp)

poss5 = []

for x in xrange(0,len(poss7),1): 
	newlst = []
	templst = []
	for i in range(len(str(poss7[x]))): 
		templst.append(int(str(poss7[x])[i]))
	newlst = list(lst[y] for y in xrange(0,len(lst),1) if lst[y] not in templst)
	for i in xrange(0,len(newlst),1):
		temp = str(newlst[i]) + poss7[x]
		if int(temp[:3])%5 == 0: 
			poss5.append(temp)

poss3 = []

for x in xrange(0,len(poss5),1): 
	newlst = []
	templst = []
	for i in range(len(str(poss5[x]))): 
		templst.append(int(str(poss5[x])[i]))
	newlst = list(lst[y] for y in xrange(0,len(lst),1) if lst[y] not in templst)
	for i in xrange(0,len(newlst),1):
		temp = str(newlst[i]) + poss5[x]
		if int(temp[:3])%3 == 0: 
			poss3.append(temp)

poss2 = []

for x in xrange(0,len(poss3),1): 
	newlst = []
	templst = []
	for i in range(len(str(poss3[x]))): 
		templst.append(int(str(poss3[x])[i]))
	newlst = list(lst[y] for y in xrange(0,len(lst),1) if lst[y] not in templst)
	for i in xrange(0,len(newlst),1):
		temp = str(newlst[i]) + poss3[x]
		if int(temp[:3])%2 == 0: 
			poss2.append(temp)

poss1 = []

for x in xrange(0,len(poss2),1): 
	newlst = []
	templst = []
	for i in range(len(str(poss2[x]))): 
		templst.append(int(str(poss2[x])[i]))
	newlst = list(lst[y] for y in xrange(0,len(lst),1) if lst[y] not in templst)
	for i in xrange(0,len(newlst),1):
		temp = str(newlst[i]) + poss2[x]
		poss1.append(int(temp))
			
print poss2
print poss1
print sum(poss1)
			
print('Solution took: ' + str(dt.now()-start) + ' ms')
