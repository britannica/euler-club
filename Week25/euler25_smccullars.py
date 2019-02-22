def next_fibonacci(x):
    return (x[1], x[0] + x[1])

n = 1
f = (0,1)

while len(str(f[1])) < 1000:
    f = next_fibonacci(f)
    n += 1

print(n)
