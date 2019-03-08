import math

# re-using my solution for week 7
def is_prime(x):
    for n in range(math.ceil(math.sqrt(abs(x))), 1, -1):
        if x % n == 0:
            return False
    return True

def calculate_quadratic(a,b,n):
    return n**2 + a*n + b

def consecutive_primes(a,b):
    n = 0
    while is_prime(calculate_quadratic(a,b,n)):
        n += 1
    return n

answer = ()
max_consecutive_primes = 0
for a in range(-999, 1000):
    for b in range(-1000, 1001):
        cp = consecutive_primes(a,b)
        if cp > max_consecutive_primes:
            max_consecutive_primes = cp
            answer = (a,b)

print(answer[0] * answer[1])
