#Project Euler Problem 69
#looking at some patters on Wiki; we need to find the phi that is produced as a result of products of primes because this will result in a maximum n and a minimum phi. The phis for primes are tiny.
#these are the prime numbers whose product is greater than 1e6; they're the only ones we'll need. The code will print the result before 19 is used because the product that uses all primes is greater than 1e6
primes = [2, 3, 5, 7, 11, 13, 17, 19]
result = 1
upper_lim = int(1e6)
for p in primes:
    if p*result > upper_lim:
        print "the max. n/phi occurs for n = ", result
    result *= p