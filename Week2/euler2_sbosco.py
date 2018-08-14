# Euler Club, week 2 
    
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)

i = 1 
evens = 0
while 1==1: 
    f = fib(i) 
    if f > 4000000:
        break
    print(f)
    if f%2 == 0:
        evens += f 
    i += 1
print('evens total={0}'.format(evens))