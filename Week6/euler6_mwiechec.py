from functools import reduce
import operator

naturals = range(1,101)
squares = [x**2 for x in naturals]
sum_naturals = reduce(operator.add, naturals)
sum_squares = reduce(operator.add, squares)
answer = sum_naturals ** 2 - sum_squares

print ("{} - {} = {}".format(sum_naturals ** 2, sum_squares, answer))
