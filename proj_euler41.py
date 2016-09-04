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

pandigital_list = []
i = 1000000
while True:
    if isprime(i) == True:
        check_set = set('1234567')
        numba = set(str(i))
        if len(check_set & numba) == 7:
            pandigital_list.append(i)
            print pandigital_list
    i += 1
    if i == 10000000:
        break

#kind of an ugly brute force method, all pandigitals seem to have either 4 or 7 numbers
    
    
    
    