import numpy as np
import time
t = time.time()
numbers_list = [0]
factors_list = [0]

def factors(n):
    n_factors = 0 #waay too slow
    for i in range(1,int(np.ceil(np.sqrt(n)))):
        if n%i == 0:
            n_factors += 1
    return n_factors*2

while factors_list[-1] <= 500:
    numbers_list.append(sum(range(len(numbers_list)+1)))
    factors_list.append(factors(numbers_list[-1]))

print numbers_list[-1]
elapsed = time.time() - t
print elapsed