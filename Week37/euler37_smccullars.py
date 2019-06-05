####### begin sieve generation of primes #######

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

####### end sieve generation of primes #######

def truncate(d, reverse=False):
    return int(str(d)[:-1]) if reverse else int(str(d)[1:])

def is_truncatable(p, reverse=False):
    if p not in primes:
        return False
    if len(str(p)) == 1:
        return True
    return is_truncatable(truncate(p, reverse=reverse), reverse=reverse)

truncatable_primes = []

for prime in sorted(list(primes)):
    if prime > 7 and is_truncatable(prime) and is_truncatable(prime, reverse=True):
        truncatable_primes.append(prime)
        
    if len(truncatable_primes) == 11:
        break

print(sum(truncatable_primes))
