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

i = 0
prime_list = []
remainder = 0
while remainder <= 1e10:
    if isprime(i) == True:
        prime_list.append(i)
        remainder = ((i - 1)**len(prime_list) + (i + 1)**len(prime_list))%(i**2) 
    i += 1
print len(prime_list)
print prime_list[-1]

#sript is a little slow