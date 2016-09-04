import numpy as np

values = np.zeros(100)
values[0:19] = 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8

for i in range(20,100): #index 100 means it ends at 99
    current = 0
    for j in range(len(str(i))):
        if len(str(i)) == 2:
            if j == 0:
                if str(i)[j] == '2':
                    current += 6 #twenty
                if str(i)[j] == '3':
                    current += 6 #thirty
                if str(i)[j] == '4':
                    current += 5 #forty
                if str(i)[j] == '5':
                    current += 5 #fifty
                if str(i)[j] == '6':
                    current += 5 #sixty
                if str(i)[j] == '7':
                    current += 7 #seventy
                if str(i)[j] == '8':
                    current += 6 #eighty
                if str(i)[j] == '9':
                    current += 6 #ninety
            
            if j == 1:
                if str(i)[j] == '0':
                    current += 0 #not pronounced
                if str(i)[j] == '1':
                    current += 3 #one
                if str(i)[j] == '2':
                    current += 3 #two
                if str(i)[j] == '3':
                    current += 5 #three
                if str(i)[j] == '4':
                    current += 4 #four
                if str(i)[j] == '5':
                    current += 4 #five
                if str(i)[j] == '6':
                    current += 3 #six
                if str(i)[j] == '7':
                    current += 5 #seven
                if str(i)[j] == '8':
                    current += 5 #eight
                if str(i)[j] == '9':
                    current += 4 #nine
                    
    values[i-1] += current

#the last one, 99 is the 98th index

values100 = values + 13
values100[99] -= 3

values200 = values + 13
values200[99] = 12

values300 = values + 15
values300[99] = 11

values400 = values + 14
values400[99] = 11

values500 = values + 14
values500[99] = 10

values600 = values + 13
values600[99] = 12

values700 = values + 15
values700[99] = 12

values800 = values + 15
values800[99] = 11

values900 = values + 14
#values900[99] -= 3
values900[99] = 11 #one thousand

values[99] += 10

print sum(values)
print values
print sum(values) + sum(values100) + sum(values200) + sum(values300) + sum(values400) + sum(values500) + sum(values600) + sum(values700) + sum(values800) + sum(values900) 
