from fractions import Fraction
alist = []
for i in range(1,10):
    for j in range(1,10):
        for k in range(1,10):
            if float(str(i)+str(j))/float(str(j)+str(k)) == float(i)/float(k) and float(i)/float(k) != 1.0:
                alist.append(float(i)/float(k))
            if float(str(i)+str(j))/float(str(k)+str(j)) == float(i)/float(k) and float(i)/float(k) != 1.0:
                alist.append(float(i)/float(k))
            if float(str(j)+str(i))/float(str(j)+str(k)) == float(i)/float(k) and float(i)/float(k) != 1.0:
                alist.append(float(i)/float(k))
alist = sorted(set(alist))
print len(alist)
print alist
