# Euler 12 - Kunal Sen
# Nth Triangular number is N(N+1)/2
#   if N is even then Nth number is product of two integers a = N/2 and b = (N+!)
#   if N is odd then Nth number is product of two integeres a = N and b = (N+!)/2
# f1 = factors of a
# f2 = factors of b
# then factors of a*b is f1 U f2 U f1*f2
# where f1*f2 is the set of all possible pairwise products between f1 and f2

def Factors(N):
    f = {1, N}
    for i in range(2, N // 2 +1):
        if N % i == 0:
            f.add(i)
    return f


def TF(N):
    if N % 2 == 0:
        f1 = Factors(N // 2)
        f2 = Factors(N + 1)
    else:
        f1 = Factors(N)
        f2 = Factors((N + 1) // 2)
    f = f1.union(f2)
    for i in f1:
        for j in f2:
            f.add(i*j)
    return len(f)


for i in range(1, 20000):
    x = TF(i)
    if x > 500:
        print (i, x)
        break
