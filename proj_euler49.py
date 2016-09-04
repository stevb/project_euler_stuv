import numpy as np
def isprime(n):
    n = abs(int(n))
    
    if n < 2:
        return False
    
    if n == 2:
        return True
    
    if not n & 1:
        return False
    
    for x in range(3, int(n**0.5) + 1, 2):
        if n % x == 0:
            return False
    
    return True

for i in xrange(1000,10000):
    if isprime(i) == True:
        for j in xrange(1, int(np.floor((10000. - i)/2))):
            if isprime(i + j) == True and isprime(i + 2*j) == True:
                #print [i, i+j, i+2*j]
                if (sorted(str(i)) == sorted(str(i + j)) == sorted(str(i + 2*j))) == True:
                    print [i, i+j, i+2*j]
                