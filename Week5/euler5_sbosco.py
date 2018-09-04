# euler 5

from functools import reduce

def primes(n):
    primfac = []
    d = 2
    while d*d <= n:
        while (n % d) == 0:
            primfac.append(d)  
            n //= d
        d += 1
    if n > 1:
       primfac.append(n)
    return primfac
    
def insertprimes(allfacs, primfacs):
    for j in allfacs:
#        print('j',j, primfacs)
        try:
            primfacs.remove(j)
        except:
            pass
    allfacs = allfacs + primfacs
#    print ('A', primfacs, allfacs)
    return allfacs
 
    
allfacs = []
for i in range(2, 21):
    primfacs = primes(i)
    allfacs = insertprimes(allfacs, primfacs)
#    print (i, primfacs, allfacs)

print(reduce(lambda x, y: x*y, allfacs))
