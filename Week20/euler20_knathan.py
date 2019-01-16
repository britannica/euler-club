import math
n = int(input ("Enter the value of N : "))
fact = math.factorial(n)

def num_sum (fact):
   summation = 0
   while fact > 0:
#       print (fact % 10)
       summation = summation + fact % 10
       fact = fact //10
#       print(summation)
#       print(fact)
   return summation


print ("Factorial of ", n," is : ", fact)
print ("Sum of the digits in the factorial of number ", n," is : ", num_sum(fact))


