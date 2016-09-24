#proj_euler69.py
import numpy as np
from fractions import gcd

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

to_val = 1e6   
primes_list = []
global primes_list
for i in range(2,int(to_val)):
    if isprime(i) == True:
        primes_list.append(i) 
def totient(n, the_list):
    #wikipedia Euler's Tolient function
    #I like Python's list comprehension
    #p are distinct prime factors
    phi = [(1-1./p) for p in the_list if n%p == 0]
    return n*np.prod(phi)    
phi_list = []
sol_list = []
vals = []
for n in range(2,int(to_val)):
    vals.append(n)
    phi_list.append(totient(vals[-1], [x for x in primes_list if x<=(vals[-1])]))
    sol_list.append((vals[-1])/phi_list[-1])
print "winner: ", vals[sol_list.index(max(sol_list))] 
print "phi is: ", phi_list[sol_list.index(max(sol_list))] 
print "n/phi is: ", sol_list[sol_list.index(max(sol_list))] 