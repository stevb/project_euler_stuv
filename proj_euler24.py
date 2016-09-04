import itertools
import time
t = time.time()
numbers = [0,1,2,3,4,5,6,7,8,9]
alist = []
for subset in itertools.permutations(numbers, len(numbers)):
    alist.append(subset)
alist.sort()
print alist[999999]
elapsed = time.time() - t
print elapsed