#proj_euler92.py
from itertools import product
def number_chain(number):
    #val_list = map(int,str(number))
    #return sum(map(lambda x:x*x, map(int,str(number))))
    
    #avoids recasting to string
    sol = 0
    while number:
        sol += (number%10)**2
        number = number//10
    return sol
chain_89 = []
chain_1 = []

numbers = ['0','1','2','3','4','5','6','7','8','9']
number_list = [''.join(i) for i in product(numbers,repeat=7)]
#number_list = list(set(number_list))
#join(sorted(str)) for str in number_list
#for str in number_list: 
#    str = ''.join(sorted(str))
#number_list = sorted(number_list)
number_list = [''.join(sorted(i)) for i in number_list] #'alphebetize' all individual strings
number_list = list(set(number_list)) #delete duplicates
number_list = sorted(number_list) #'alphebetize all elements in list'
number_list = map(int, number_list) #cast all strings to ints
number_list.remove(0) #remove zero from number_list
print len(number_list)
#print number_list
n_start_89 = 0
n_start_1 = 0
#number_list = list(range(1,100,1))
#print number_list
#val = [1,2,3,4,5,6,7,8,9,10]
#while len(number_list) > 0:
for value in number_list:
    #chain = [number_list[0]]
    chain = [value]
    #print chain[0]
    while True:
        ans = number_chain(chain[-1])
        if ans == 89:
            chain.append(ans)
            chain_89 += chain
            n_start_89 += len(str(value))**2
            #print chain
            break
        if ans == 1:
            chain.append(ans)
            chain_1 += chain
            n_start_1 += len(str(value))**2
            #start_1.append(chain[0])
            #print chain
            break
        chain.append(ans)
    #number_list = [i for i in number_list if i not in chain]
#print number_list
chain_89 = list(set(chain_89)) #delete duplicates
chain_1  = list(set(chain_1))

#print len(sorted(set(chain_89)))
#print start_89
#print start_1
#print len(start_1)
print n_start_89