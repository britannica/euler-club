max_number = 2000000

not_primes = set()

for x in range(2,max_number):
    for not_prime in range(2*x, max_number, x):
        not_primes.add(not_prime)

sieve = [x for x in range(2,max_number) if x not in not_primes]

print(sum(sieve))
