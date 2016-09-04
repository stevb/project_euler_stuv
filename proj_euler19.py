alist = [['Tuesday', 1, 'January', 1901]]
n_special_sundays = 0

while alist[-1][3] != 2001: 
    next_day = ['',0,'',0]

    if alist[-1][0] == 'Monday':
        next_day[0] = 'Tuesday'
    if alist[-1][0] == 'Tuesday':
        next_day[0] = 'Wednesday'
    if alist[-1][0] == 'Wednesday':
        next_day[0] = 'Thursday'
    if alist[-1][0] == 'Thursday':
        next_day[0] = 'Friday'
    if alist[-1][0] == 'Friday':
        next_day[0] = 'Saturday'
    if alist[-1][0] == 'Saturday':
        next_day[0] = 'Sunday'
    if alist[-1][0] == 'Sunday':
        next_day[0] = 'Monday'

    if alist[-1][2] == 'January' and alist[-1][1] < 31:
        next_day[1] = alist[-1][1] + 1
        next_day[2] = alist[-1][2]
        next_day[3] = alist[-1][3]
    if alist[-1][2] == 'January' and alist[-1][1] == 31:
        next_day[1] = 1
        next_day[2] = 'February'
        next_day[3] = alist[-1][3]
    
    if alist[-1][2] == 'February' and alist[-1][1] < 28:
        next_day[1] = alist[-1][1] + 1
        next_day[2] = alist[-1][2]
        next_day[3] = alist[-1][3]
    if alist[-1][2] == 'February' and alist[-1][1] == 29:
        next_day[1] = 1
        next_day[2] = 'March'
        next_day[3] = alist[-1][3]
    if alist[-1][2] == 'February' and alist[-1][1] == 28 and alist[-1][3]%4 != 0:
        next_day[1] = 1
        next_day[2] = 'March'
        next_day[3] = alist[-1][3]
    if alist[-1][2] == 'February' and alist[-1][1] == 28 and alist[-1][3]%4 == 0:
        next_day[1] = 29
        next_day[2] = 'February'
        next_day[3] = alist[-1][3]
    
    if alist[-1][2] == 'March' and alist[-1][1] < 31:
       next_day[1] = alist[-1][1] + 1
       next_day[2] = alist[-1][2]
       next_day[3] = alist[-1][3]
    if alist[-1][2] == 'March' and alist[-1][1] == 31:
       next_day[1] = 1
       next_day[2] = 'April'
       next_day[3] = alist[-1][3]
   
    if alist[-1][2] == 'April' and alist[-1][1] < 30:
       next_day[1] = alist[-1][1] + 1
       next_day[2] = alist[-1][2]
       next_day[3] = alist[-1][3]
    if alist[-1][2] == 'April' and alist[-1][1] == 30:
       next_day[1] = 1
       next_day[2] = 'May'
       next_day[3] = alist[-1][3]

    if alist[-1][2] == 'May' and alist[-1][1] < 31:
       next_day[1] = alist[-1][1] + 1
       next_day[2] = alist[-1][2]
       next_day[3] = alist[-1][3]
    if alist[-1][2] == 'May' and alist[-1][1] == 31:
       next_day[1] = 1
       next_day[2] = 'June'
       next_day[3] = alist[-1][3]

    if alist[-1][2] == 'June' and alist[-1][1] < 30:
       next_day[1] = alist[-1][1] + 1
       next_day[2] = alist[-1][2]
       next_day[3] = alist[-1][3]
    if alist[-1][2] == 'June' and alist[-1][1] == 30:
       next_day[1] = 1
       next_day[2] = 'July'
       next_day[3] = alist[-1][3]
    
    if alist[-1][2] == 'July' and alist[-1][1] < 31:
        next_day[1] = alist[-1][1] + 1
        next_day[2] = alist[-1][2]
        next_day[3] = alist[-1][3]
    if alist[-1][2] == 'July' and alist[-1][1] == 31:
        next_day[1] = 1
        next_day[2] = 'August'
        next_day[3] = alist[-1][3]
    
    if alist[-1][2] == 'August' and alist[-1][1] < 31:
        next_day[1] = alist[-1][1] + 1
        next_day[2] = alist[-1][2]
        next_day[3] = alist[-1][3]
    if alist[-1][2] == 'August' and alist[-1][1] == 31:
        next_day[1] = 1
        next_day[2] = 'September'
        next_day[3] = alist[-1][3]
    
    if alist[-1][2] == 'September' and alist[-1][1] < 30:
        next_day[1] = alist[-1][1] + 1
        next_day[2] = alist[-1][2]
        next_day[3] = alist[-1][3]
    if alist[-1][2] == 'September' and alist[-1][1] == 30:
        next_day[1] = 1
        next_day[2] = 'October'
        next_day[3] = alist[-1][3]
   
    if alist[-1][2] == 'October' and alist[-1][1] < 31:
        next_day[1] = alist[-1][1] + 1
        next_day[2] = alist[-1][2]
        next_day[3] = alist[-1][3]
    if alist[-1][2] == 'October' and alist[-1][1] == 31:
        next_day[1] = 1
        next_day[2] = 'November'
        next_day[3] = alist[-1][3]
    
    if alist[-1][2] == 'November' and alist[-1][1] < 30:
        next_day[1] = alist[-1][1] + 1
        next_day[2] = alist[-1][2]
        next_day[3] = alist[-1][3]
    if alist[-1][2] == 'November' and alist[-1][1] == 30:
        next_day[1] = 1
        next_day[2] = 'December'
        next_day[3] = alist[-1][3]
    
    if alist[-1][2] == 'December' and alist[-1][1] < 31:
        next_day[1] = alist[-1][1] + 1
        next_day[2] = alist[-1][2]
        next_day[3] = alist[-1][3]
    if alist[-1][2] == 'December' and alist[-1][1] == 31:
        next_day[1] = 1
        next_day[2] = 'January'
        next_day[3] = alist[-1][3] + 1

    alist.append(next_day)
    if alist[-1][0] == 'Sunday' and alist[-1][1] == 1:
        n_special_sundays += 1

print alist
print n_special_sundays
