months_that_start_with_sundays = 0
total_days = 0

days = ['mon','tue','wed','thu','fri','sat','sun']
months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']

for year in range(1900,2001):
    for month in months:
        if year in range(1901,2001) and days[total_days % 7] == 'sun':
            months_that_start_with_sundays += 1

        if month in ['sep','apr','jun','nov']:
            total_days += 30
        elif month == 'feb':
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                total_days += 29
            else:
                total_days += 28
        else:
            total_days += 31

print(months_that_start_with_sundays)
        
