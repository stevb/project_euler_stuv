#proj_euler52.py
n = 1
while True:
    nr = int(''.join(sorted(str(n)))) #reordered n
    n2 = int(''.join(sorted(str(2*n))))
    n3 = int(''.join(sorted(str(3*n))))
    n4 = int(''.join(sorted(str(4*n))))
    n5 = int(''.join(sorted(str(5*n))))
    n6 = int(''.join(sorted(str(6*n))))
    
    n_list = [nr,n2,n3,n4,n5,n6]
    if len(set(n_list)) == 1:
        print n #found solution is 142857, takes about a second or three
        break
    n += 1