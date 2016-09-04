alist = [1,1,2]
while len(str(alist[-1])) < 1000:
    alist.append(alist[-1] + alist[-2])
print len(alist)