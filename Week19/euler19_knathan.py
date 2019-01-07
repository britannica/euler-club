from datetime import date

#i = 1
sunday = 0

for year in range(1901, 2001):
    for month in range(1, 13):
        day = date(year, month, 1)
#        if i < 50:
#            print (day)
#            print (day.weekday())
#            i = i+1
        if day.weekday() == 6:
            sunday = sunday + 1

print ("Number of Sundays that fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000): ",sunday)
