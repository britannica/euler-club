from math import floor

def find_divisors(num):
    #every number is divisible by one and itself
    divisors = {1, num}
    maximum_possible_divisor = floor(num/2) + 1
    for i in range(2, maximum_possible_divisor):
        if i not in divisors and num % i == 0:
            divisors.add(i)
            divisors.add(int(num/i))
    return divisors

def calculate_triangle_number(n):
    return sum([i for i in range(1,n+1)])

x = 2
while True:
    triangle_number = calculate_triangle_number(x)
    divisors = find_divisors(triangle_number)
    if len(divisors) > 500:
        print('x:             ' + str(x))
        print('triangle num:  ' + str(triangle_number))
        print('divisor count: ' + str(len(divisors)))
        print('divisors:      ' + str(sorted(divisors)))
        print('--------------------------------')
        break
    x += 1
