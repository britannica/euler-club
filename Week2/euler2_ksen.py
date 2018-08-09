S = 2
A = 1
B = 2
while True:
    C = A+2*B
    D = 2*A+3*B
    if(D>4000000):
        break
    S = S+D
    A = C
    B  = D
print (S) 
