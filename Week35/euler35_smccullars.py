MAX_PRIME = 1000000

# initialize sieve
sieve = [None] * MAX_PRIME
# zero and one are not primes
sieve[0] = False
sieve[1] = False

# populate the sieve
for x in range(2,MAX_PRIME):
    if sieve[x] is None:
        sieve[x] = True
    for y in range(x*2, MAX_PRIME, x):
        sieve[y] = False

# turn the sieve into a set of primes for convenience
primes = set(n for n,is_prime in enumerate(sieve) if is_prime)

circular_count = 0

for p in primes:
    is_circular = True
    p_digits = list(str(p))
    for n in range(0, len(p_digits)):
        rotation = p_digits[n:] + p_digits[0:n]
        rotated_digit = int(''.join(rotation))
        if rotated_digit not in primes:
            is_circular = False
    if is_circular:
        circular_count += 1

print(circular_count)
