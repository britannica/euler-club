def proper_divisors(n):
    pd = []
    for x in range(1,n):
        if n % x == 0:
            pd.append(x)
    return pd

amicable_numbers = []
divisor_sums = {}
for x in range(1, 10000):
    y = sum(proper_divisors(x))
    if y in divisor_sums and x == divisor_sums[y] and x != y:
            amicable_numbers.extend([x,y])
    else:
        divisor_sums[x] = y

print(sum(amicable_numbers))
