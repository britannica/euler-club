n = 1

a = 0
b = 1

while len(str(b)) < 1000:
    a,b = b,a+b
    n += 1

print(n)
