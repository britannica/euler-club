import math


def is_prime(x):
    for n in range(math.ceil(math.sqrt(x)), 1, -1):
        if x % n == 0:
            return False
    return True


prime_count = 1
x = 2

while prime_count < 10001:
    x += 1
    if is_prime(x):
        prime_count += 1

print(x)
