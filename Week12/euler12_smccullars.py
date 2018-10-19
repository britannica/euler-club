from functools import reduce
from math import floor, sqrt
from operator import mul


#recycled from my solution to week 10 via the sieve of eratosthenes
def generate_primes(max_number):
    #index is offset by 2..ie. the sieve's position 0 is 2, position 1 is 3, etc.
    sieve = [True for x in range(2,max_number)]

    for x in range(2,floor(sqrt(max_number))):
        for not_prime in range(2*x, max_number, x):
            sieve[not_prime-2] = False

    return [x+2 for x in range(0, len(sieve)) if sieve[x]]


def factorize(num, primes):
    factorization = {}
    for prime in primes:
        if num == 1:
            return factorization
        if num % prime == 0:
            if prime in factorization:
                factorization[prime] += 1
            else:
                factorization[prime] = 1
            num = int(num/prime)
            while num % prime == 0:
                factorization[prime] += 1
                num = int(num/prime)
    return factorization


primes = generate_primes(1000)

n = 1
while True:
    triangle_number = sum([i for i in range(1,n+1)])
    factorization = factorize(triangle_number, primes)

    divisor_count = reduce(mul, [int(exponent+1) for exponent in factorization.values()], 1)
    if divisor_count > 500:
        print('n:             ' + str(n))
        print('triangle num:  ' + str(triangle_number))
        print('factorization: ' + str(factorization))
        print('divisor count: ' + str(divisor_count))
        break
    n += 1
