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

# turn the sieve into an ordered (ascending) list of primes for convenience
primes = set(n for n,is_prime in enumerate(sieve) if is_prime)


def is_truncatable(p, direction):
    if p in primes:
        if len(str(p)) > 1:
            if direction == 'both':
                return is_truncatable(int(str(p)[1:]), 'left') and is_truncatable(int(str(p)[:-1]), 'right')
            elif direction == 'left':
                return is_truncatable(int(str(p)[1:]), direction)
            elif direction == 'right':
                return is_truncatable(int(str(p)[:-1]), direction)
        else:
            return True
    return False


truncatable_primes = []

for prime in sorted(list(primes)):
    if prime > 7 and is_truncatable(prime, 'both'):
        truncatable_primes.append(prime)
        
    if len(truncatable_primes) == 11:
        print(sum(truncatable_primes))
        break
