factorials = {}

for x in range(0,10):
    factorials[x] = x * factorials[x-1] if x-1 in factorials else 1

curious_number_total = 0

for x in range(3, 100000):
    factorial_sum = 0
    for n in list(str(x)):
        factorial_sum += factorials[int(n)]
    if factorial_sum == x:
        curious_number_total += x

print(curious_number_total)
