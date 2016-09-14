#proj_euler38.py

#Possible combinations of nine digit pandigital numbers is 9! = 362880. Going to try to create all possible iterations using itertools/permutations.

from itertools import permutations
pan_list = map(int, [''.join(p) for p in permutations('123456789')])
#could reduce the size of pan_list by getting rid of the small stuff

#This means that the largest pandigital numbers will be at the end of the pan_list
#moving through, you'd have to recognize that the second part of the pandigital is a factor of the first.
#the first int will be 4 numbers, then the second part will be times 2 and would be 5. 
#So first part is 4 digits and starts with 9
#The range to test is then from 9123 to 9876
pan_found = []
for i in range(9123,9876):
    if int(str(i) + str(i*2)) in pan_list: #this is slow and I'd like to do it without casting to a string :/ How can I do that?
        pan_found.append(int(str(i) + str(i*2)))
print pan_found
print max(pan_found)
