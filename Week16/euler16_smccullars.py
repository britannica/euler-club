# calculate the exponent, make it a string, make that a list of characters, 
# use list comprehension to make it a list of integers, sum that list, 
# and then print the total
print(sum([int(x) for x in list(str(2**1000))]))
