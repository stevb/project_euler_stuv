#proj_euler27.py

import numpy as np

def isprime(number):
    prime = False
    if number > 1:
        prime = True
        q = 2
        red =  number**0.5 
        while q <= red and prime == True:
            if number % q == 0:
                prime = False
            q += 1
    return prime

#the problem can be reduced a bit. It's known that at n = 0, 0 + 0 + b = prime, so b must be prime. When n = 1, because all primes, except for 2, must be odd, a must be odd by the relation that, 1 + a + b = prime and b is already prime and odd. So possible b values are from -999 to 999 and possible a values are all odd numbers in that range. 

a = np.linspace(-999, 999, 1000)
b = []
for i in range(1000):
    if isprime(i):
        b.append(i)
        b.append(-i)

n_max = 0
a_max = 0
b_max = 0
for i in a:
    for j in b:
        n = 0
        while isprime(n**2 + i*n + j):
                if n_max < n:
                    n_max = n
                    a_max = i
                    b_max = j
                n += 1
print n_max
print a_max
print b_max