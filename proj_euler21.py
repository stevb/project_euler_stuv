#proj_euler21.py

import numpy as np

max_val =  10000

sums = np.zeros([max_val,2])
for i in range(1,max_val): #if going to 10, enter 11? Python indexing
    sums[i,0] = i
    current_sum = 0
    for j in range(1,i):
        if i%j == 0:
            current_sum += j
    sums[i,1] = current_sum
    
amicable_pair_sum = 0

for i in range(len(sums)):
    if sums[i,1] < max_val and sums[i,0] != sums[i,1]:
        if sums[i,0] == sums[sums[i,1],1] and sums[i,1] == sums[sums[i,0],1]:
            print "pair found ", sums[i], "and ", sums[sums[i,1]] #pairs will be printed twice
            amicable_pair_sum += i

print amicable_pair_sum
#correct answer is 31626