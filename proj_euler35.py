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

alist = []

for i in range(0,1000000):
    if isprime(i) == True:
        k = 0
        for j in range(0,len(str(i))):
            if isprime(str(i)[j:] + str(i)[:j]):
                k += 1
                if k == len(str(i)):
                    alist.append(i)

print alist
print len(alist)