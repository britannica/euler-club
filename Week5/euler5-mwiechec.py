
def get_prime_factors(x):
    z = (x // 2) + 1
    for p in range(2,z):
        if (x % p) == 0:
            x = x // p
            if x == 1:
                return [p]
            else:
                res = get_prime_factors(x)
                res.append(p)
                return res
    else:
        return [1,x]

def get_all_factors(x):
    factors = []                        # array to hold prime factors
    for x in range(1, x):              # spin through 1 through 20
        base = factors.copy()           # remember what we have so far
        primes = get_prime_factors(x)   # get the prime factors

        # see what additional prime factors we still have not found by subtraction
        additional = [item for item in primes if item not in factors or factors.remove(item)]
        factors = base + additional     # create a new list of factors
    return factors

factors = get_all_factors(20)
print (factors)

# multiply for solution
product = 1
for x in factors:
    product *= x
print (product)
