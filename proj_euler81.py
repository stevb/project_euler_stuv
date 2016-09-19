#proj_euler81.py
#dynamic programming, like an elephant, never forget!

import numpy as np
matrix = np.loadtxt('p081_matrix.txt', delimiter = ',')

rows = len(matrix)
cols = len(matrix[0])
for i in range(rows-1,-1,-1):
    for j in range(cols-1,-1,-1):
        #print i,j
        if i == rows - 1 and j == cols - 1:
            print "start"
            #break
        elif i == rows - 1:
            matrix[i][j] += matrix[i][j+1] #bottom bound
        elif j == cols - 1:
            matrix[i][j] += matrix[i+1][j] #right bound
        else:
            matrix[i][j] += min(matrix[i+1][j], matrix[i][j+1]) #can go both directions
print matrix[0][0] #result = 427337