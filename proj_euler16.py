number, alist = str(2**1000), []
for i in range(len(str(number))):
    alist.append(int(number[i]))
print sum(alist)