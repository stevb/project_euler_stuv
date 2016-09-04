import numpy as np
alist = []
number = 3
while True:
    value = 0
    for i in range(0,len(str(number))):
        value += np.math.factorial(int(str(number)[i]))
    if value == number:
        alist.append(number)
        print alist
        print sum(alist)
    number += 1
#There are two numbers total; 145 and 40585 summing 40730