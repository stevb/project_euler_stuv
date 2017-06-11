#Project Euler Problem 31

#target = 200
#coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 10
coins  = [1,2,5,10]
ways = [1] + [0]*target

for coin in coins:
    for i in range(coin, target+1):
        ways[i] += ways[i-coin]

print "Ways to make change =", ways[target]
#answer is 73682
#1111111111
#111111112
#11111122
#111115
#1225
#11125
#55
#10
#22222
#222211
#2221111