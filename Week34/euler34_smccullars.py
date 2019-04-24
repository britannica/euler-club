from math import factorial

total = 0

for x in range(3, 100000):
    factorial_sum = 0
    for n in list(str(x)):
        if x >= factorial_sum:
            factorial_sum += factorial(int(n))
    if factorial_sum == x:
        total += x

print(total)
