
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


print (get_prime_factors(600851475143))
# [1, 6857, 1471, 839, 71]
