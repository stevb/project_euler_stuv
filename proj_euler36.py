alist = []
for i in range(0,1000000):
    if str(i) == str(i)[::-1]:
        if str('{0:b}'.format(i)) == str('{0:b}'.format(i))[::-1]:
            alist.append(i)
print alist
print sum(alist)