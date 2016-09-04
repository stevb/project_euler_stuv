names = open('p022_names.txt').read().replace('"','').split(',')

def value_name(astring):
    value = 0
    for j in range(0,len(astring)):
        value += ord(astring[j]) - 64
    return value

names.sort()

values = []
for i in range(0,len(names)):
    values.append(value_name(names[i])*(i+1))
    
print sum(values)