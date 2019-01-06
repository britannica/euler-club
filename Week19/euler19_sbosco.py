# euler19

import time
t0 = time.time()
TREE_SIZE = 15

regDaysInMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leapDaysInMonth = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
sundayCount = 0
monthFirstDay = 1

for year in range (1900, 2001):
    for month in range (0, 12):
        daysInMonth = regDaysInMonth
        if year % 100 == 0:
            if year % 400 == 0:
                daysInMonth = leapDaysInMonth
        elif year % 4 == 0:
            daysInMonth = leapDaysInMonth
        monthFirstDay = (monthFirstDay + daysInMonth[month]) % 7
        if monthFirstDay == 0:
            if year > 1900:
                sundayCount+= 1
            
print('Months beginning with Sunday=', sundayCount)

t1 = time.time()
elapsed = t1 - t0
print('time=', elapsed)



# Months beginning with Sunday= 171
# time= 0.0009999275207519531
