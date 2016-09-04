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
i = 8 #It was stated that we are not interested in 2,3,5, or 7
while len(alist) < 11:
    if isprime(i) == True:
        k = 0
        for j in range(0, len(str(i))):
            if isprime(int(str(i)[0:len(str(i)) - j])) == True and isprime(int(str(i)[j:len(str(i))])) == True:
                k += 1
                if k == len(str(i)):
                    alist.append(i)
    i += 1
            

print alist
print len(alist)
print sum(alist)