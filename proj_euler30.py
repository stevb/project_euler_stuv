number = 2 #start at 2 to avoid 0 and 1
alist = []
while True:
    current_sum = 0
    for i in range(0,len(str(number))):
        current_sum += int(str(number)[i])**5
    
    if current_sum == number:
        alist.append(number)
        print alist
        print sum(alist)
    number += 1