pandigital_multiples = {}

for n in range(2,9999):
    x = 1
    candidate = ''
    while len(candidate) < 9:
        candidate += str(n*x)
        x += 1
    if len(candidate) == 9 and '0' not in candidate and len(set(list(candidate))) == 9:
        pandigital_multiples[n] = candidate

print(max(pandigital_multiples.values()))
