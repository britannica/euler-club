sum_of_squares = 0
sum_to_be_squared = 0

for i in range(1, 101):
    sum_of_squares += i ** 2
    sum_to_be_squared += i

difference = (sum_to_be_squared ** 2) - sum_of_squares
print("sum square difference is: ", difference)
