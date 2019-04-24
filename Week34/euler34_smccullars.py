from math import factorial

total = 0

for x in range(3, 100000):
    target = x
    for n in list(str(x)):
        if target >= 0:
            target -= factorial(int(n))
    if target == 0:
        total += x

print(total)
