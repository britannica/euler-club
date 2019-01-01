find.day.of.the.week.name <- function(input) {
  switch(input, "Monday", "Tuesday", "Wednesday", "Thursday", "Friday",  "Saturday", "Sunday")
}

find.number.of.month <- function(month) {
  if (month == 01) {
    month = 13
  }
 if (month == 02) {
    month = 14
}

  month
  
}

find.day.of.the.week <- function(day, month, year) {
  # Zeller’s Congruence
  # h = q + 13*(m+1)/5 + k + k/4 + j/4 + 5*j; 
  
  q = day #q
  m = find.number.of.month(month) #m 

  K = if(m == 13 || m == 14) (year - 1) %% 100 else year %% 100 #K
  J = if(m == 13 || m == 14) floor((year - 1) / 100) else floor(year / 100) #K

  floor1 = floor((13*(m+1))/5)
  floor2 = floor(K/4)
  floor3 = floor(J/4)

  total = (q + floor1 + K + floor2 + floor3 - 2*J) %% 7

  d = ((total + 5) %% 7 ) +1

  find.day.of.the.week.name(d)
  
}

find.is.leap.year <- function(year) {
  # year must be divisible by 4
  # years must not be divisible by 100 unless they are also divisible by 400
  if (year %% 4 == 0) {
    if (year %% 100 == 0 && year %% 400 == 0) {
     TRUE
    }
    else {
      FALSE
    }
  }
  else {
    FALSE
  }
}

#31,28,31,30,31,30,31,31,30,31,30,31

find.days.in.month <- function(month, year) {
  days = 0
  if (month == 1 || month == 3 || month == 5 || month == 7 || month ==8  || month == 10 || month == 12) {
    days = 31
  }
  else if (month == 4 || month == 6 || month == 9 || month == 11) {
    days = 30
  }
  else {
    if (find.is.leap.year(year)) {
      days = 29
    }
    else {
      #print('NOT LEAP YEAR--------------')
      days = 28
    }
  }
}

years <- c(1901:2000)
months <- c(1:12)
count = 0;
for (year in years) {
  for (month in months) {
    for (day in c(1:find.days.in.month(month, year))) {
      if (day == 1 && find.day.of.the.week(day,month,year) == "Sunday") {
        print(day)
        count = count + 1
      }
    }
  }
}

print(count)
