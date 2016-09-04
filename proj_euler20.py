import numpy
number, alist = str(numpy.math.factorial(100)), []
for i in range(len(str(number))):
    alist.append(int(number[i]))
print sum(alist)