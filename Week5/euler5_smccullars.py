from math import ceil, sqrt

# borrowed from https://codereview.stackexchange.com/questions/19509/functional-prime-factor-generator
def factor(n):
    if n <= 1: return []
    prime = next((x for x in range(2, ceil(sqrt(n))+1) if n%x == 0), n)
    return [prime] + factor(n//prime)

def factorization_to_dict(f):
    d = {}
    for fac in f:
        if d.get(fac):
            d[fac] += 1
        else:
            d[fac] = 1
    return d



factors = {}

for num in range(2,21):
    factorization = factorization_to_dict(factor(num))
    for fac, multiple in factorization.items():
        if not factors.get(fac) or factors[fac] < multiple:
            factors[fac] = multiple

smallest_multiple = 1

# and now we do a polynomial expansion
# ie. 12 == {2: 2, 3: 1} == (2 * 2) * (3) == 2 power of 2 times 3 power 1

for fac, multiple in factors.items():
    smallest_multiple *= fac ** multiple

print("smallest_multiple is: ", smallest_multiple)
