from functools import reduce

# function borrowed from Week3/euler3_mwiechec.py
# would have used my own...but alas, i did it in C
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

def factorization_to_hash(h):
    hash = {}
    for fac in h:
        if hash.get(fac):
            hash[fac] += 1
        else:
            hash[fac] = 1
    return hash

factors = {}

for num in range(2,21):
    factorization = get_prime_factors(num)
    print(num, ": " + " ".join(map(str, factorization)))
    print(factorization_to_hash(factorization))
    for fac, multiple in factorization_to_hash(factorization).items():
        if factors.get(fac):
            if factors[fac] < multiple:
                 factors[fac] = multiple
        else:
            factors[fac] = multiple

smallest_multiple = 1
for fac, multiple in factors.items():
    smallest_multiple *= fac ** multiple
print(factors)
print("smallest_multiple is: ", smallest_multiple)
