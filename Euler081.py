# coding=utf-8

# In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.
# Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.``

from datetime import datetime
start = datetime.now()

import pandas as pd
df=pd.read_csv('euler081.txt', sep=',',header=None)

for i in xrange(78,-1,-1):
    df[79][i] = df[79][i] + df[79][i+1]

for i in xrange(78,-1,-1):
    df[i][79] = df[i][79] + df[i+1][79]

for row in xrange(78,-1,-1):
    for col in xrange(78,-1,-1):
        df[row][col] += min(df[row][col+1],df[row+1][col])

print df[0][0]

print('Solution took: ' + str(datetime.now()-start) + ' ms')
