alist = []
for i in range(1000):
    alist.append((i+1)**(i+1))
print str(sum(alist))[-10:]