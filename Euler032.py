# encoding=utf-8
from datetime import datetime as dt 

start = dt.now() 

# We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.
# The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, and product is 1 through 9 pandigital.
# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.
# HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.

pandigital = [] 

def checkpan(a,b,c): 
	if (len(str(a)) + len(str(b)) + len(str(c))) <> 9: 
		return 0
	temp = [] 
	for x in xrange(0,len(str(a)),1): 
		temp.append(str(a)[x]) 
	for x in xrange(0,len(str(b)),1): 
		temp.append(str(b)[x]) 
	for x in xrange(0,len(str(c)),1): 
		temp.append(str(c)[x])
	temp = sorted(set(temp))
	if temp == ['1','2','3','4','5','6','7','8','9']:
		return 1
	
for x in xrange(1,100,1):
	for y in xrange(100,10000,1): 
		if checkpan(x,y,x*y): 
			pandigital.append(x*y)

pandigital = sorted(set(pandigital))

print sum(pandigital)

print('Solution took: ' + str(start-dt.now()) + ' ms')
