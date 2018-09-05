n = int(input ("Enter the value of N : "))
num_sum = 0
num_sum = (n*(n+1)*((2*n)+1))/6

total_square = 0
total_square = ((n* (n+1))/2)**2
print ("Square of the sum of the first ", n," natural numbers is: ", total_square)

print ("Difference between the sum of the squares of the first ", n ," natural numbers and the square of the sum is: " ,total_square - num_sum)
