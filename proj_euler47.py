#proj_euler47.py
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

def factor(number):    
    return set(reduce(list.__add__, ([i, number//i] for i in range(1, int(number**0.5) + 1) if number % i == 0)))


goal = 4
num = 640 #know that the first 3-in-a-row occurs here, so 4-in-a-row must be higher. Negligible speedup, though
results = []
while True:
    results.append(sum([isprime(x) for x in factor(num)]))
    num += 1

    if min(results[-goal:]) == goal:
        print "goal reached at starting at: ", num - goal
        break #reaches goal: 134043