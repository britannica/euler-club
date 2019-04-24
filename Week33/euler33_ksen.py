# (10a+b)/(10b+c) = a/c
# c = 10ab/(9a+b)
 
n = 1
d = 1
for a in range(1,10):
    for b in range(1,10):
        c = 10*a*b/(9*a+b)
        if int(c) == c:
            if a != b:
                n = n * (10 * a + b)
                d = d * (10 * b + c)
for i in range(1,n+1):
    if (n%i==0) & (d%1==0):
        gcd=i
        
print (d/gcd)
