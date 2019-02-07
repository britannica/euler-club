from math import ceil, sqrt

AB_LIMIT = 28124

def proper_divisors(n):
    pd = {1}
    for x in range(2,int(sqrt(n))+1):
        if n % x == 0:
            pd.add(x)
            pd.add(int(n/x))
    return pd

def is_abundant(n):
    return n < sum(proper_divisors(n))

def find_abundant_numbers():
    ab_numbers = set()
    for i in range(1, AB_LIMIT):
        if is_abundant(i):
            ab_numbers.add(i)
    return ab_numbers


ab_numbers = find_abundant_numbers()
sums_of_two_ab_numbers = set()

for x in ab_numbers:
    for y in ab_numbers:
        sums_of_two_ab_numbers.add(x+y)

total_sum = 0
for i in range(1, AB_LIMIT):
    if i not in sums_of_two_ab_numbers:
        total_sum += i

print(total_sum)
