import math

max_number = 2000000

#index is offset by 2..ie. the sieve's position 0 is 2, position 1 is 3, etc.
sieve = [True for x in range(2,max_number)]

for x in range(2,math.floor(math.sqrt(max_number))):
    for not_prime in range(2*x, max_number, x):
        sieve[not_prime-2] = False

primes = [x+2 for x in range(0, len(sieve)) if sieve[x]]
print(sum(primes))
