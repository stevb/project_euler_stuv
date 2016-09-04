#total numbers for nxn matrix is n+n-1
n = 1001
cycle_count = 0
additional = 2
alist = [1]
for i in range(1,n + n - 1):
    alist.append(alist[-1] + additional)
    cycle_count += 1
    if cycle_count == 4:
        cycle_count = 0
        additional += 2
print sum(alist)
#see that the pattern is to add two the first time around and each time around
#the amount to add increases by two as two new columns and rows are added. 