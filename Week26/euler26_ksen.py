def rec(N,D):
    Q=[]
    R=[]
    while True:
        P = N // D
        N = (N % D) * 10
        Q.append(P)
        if N == 0:
            L = 0
            break
        if R == []:
            R.append(N)
        else:
            if N in R:  
                L = len(Q) - R.index(N) - 1
                break
            else:
                R.append(N)             
    return L
                

        

max = 0
for i in range(1,1000):
    v = rec(10,i)
    if v > max:
        max = v
print (max)
