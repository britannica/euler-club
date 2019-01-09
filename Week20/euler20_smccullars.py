def factorial(x):
    return x if x == 1 else x * factorial(x-1)

# make a string from the factorial, 
# use list to chop it into characters,
# loop over the list to turn the items back into integers,
# and then sum all the integers

print(sum(int(x) for x in list(str(factorial(100)))))
        
