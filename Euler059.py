# coding=utf-8

from datetime import datetime as dt

start = dt.now()

# Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.
# A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.
# For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.
# Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.
# Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.

import csv
with open('euler059.txt', 'rb') as f:
    reader = csv.reader(f)
    x = list(reader)

# print x[0]

# print ord('a'),ord('z'), ord('A'),ord('Z'),ord(' '),ord(','),ord('.'),ord(''')
# 97 122 65 90 32 44 46 39

y = [int(x[0][i]) for i in xrange(0,len(x[0]),1)]
# print y

max1 = []
max2 = []
max3 = []

for a in xrange(97,123,1):
    temp = y[len(y)-1]^a
    print chr(temp), temp, a, chr(a)



print ord('"')
# 100 111 103 d o g

z = []


print z
o = [chr(z[i]) for i in xrange(0,len(z),1)]

print o
print sum(z)
print('Solution took: ' + str((dt.now()-start).total_seconds()) + ' seconds')
