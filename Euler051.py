# coding = utf-8

from datetime import datetime as dt

start = dt.now()

# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.

prime = []

def isprime(a):
    for i in xrange(3,int(a**0.5)+1,2):
        if a%i == 0:
            return 0
    return 1

def samedig(a):
    if len(set([str(a)[i] for i in xrange(0,len(str(a)))])) == len(str(a)):
        return 0
    return 1

i = 101

success = 0

def check(a):
    t = [str(a)[j] for j in range(0,len(str(a)))]
    for j in xrange(0,len(t)-1,1):
        if t[j] in t[j+1:]:
            s = t[j]
    if s in ('0','1','2') :
        c = 1
        l = int(s) + 1
        while l <= 9:
            t1 = []
            for z in range(0,len(t)):
                if t[z] == s:
                    t1.append(str(l))
                else:
                    t1.append(t[z])
            t2 = ''.join(t1[k] for k in range(0,len(t1)))
            if int(t2)%2 <> 0:
                if isprime(int(t2)):
                    c += 1
            l += 1
        if c == 7:
            l = int(s) + 1
            while l <= 9:
                t1 = []
                for z in range(0,len(t)):
                    if t[z] == s:
                        t1.append(str(l))
                    else:
                        t1.append(t[z])
                t2 = ''.join(t1[k] for k in range(0,len(t1)))
                if int(t2)%2 <> 0:
                    if isprime(int(t2)):
                        print a, int(t2)
                l += 1
            # print a,c
            return 1
    return 0

while success == 0:
    if samedig(i):
        if isprime(i):
            success = check(i)
    i += 2

print('Solution took: ' + str((dt.now()-start).total_seconds()) + ' seconds')


# def isprime(a):
#     for i in xrange(3,int(a**0.5)+1,2):
#         if a%i == 0:
#             return 0
#     prime.append(a)

# def check():
#     for i in xrange(0,len(prime)-8,1):
#         s = 0
#         t = [str(prime[i])[j] for j in range(0,len(str(prime[i])))]
#         for j in xrange(0,len(t)-1,1):
#             if t[j] in t[j+1:]:
#                 s = t[j]
#         if s in ('0','1','2') :
#             c = 1
#             l = int(s) + 1
#             while l <= 9:
#                 t1 = []
#                 for a in range(0,len(t)):
#                     if t[a] == s:
#                         t1.append(str(l))
#                     else:
#                         t1.append(t[a])
#                 t2 = ''.join(t1[k] for k in range(0,len(t1)))
#                 if int(t2) in prime:
#                     c += 1
#                 l += 1
#         if c == 7:
#             print prime[i]
#             # print prime
#             return 1
#     return 0
