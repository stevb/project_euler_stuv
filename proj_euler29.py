alist = []

for i in range(2,101):
    for j in range(2,101):
        alist.append(i**j)

print len(alist)
alist = sorted(set(alist)) #Removes duplicates
print len(alist)