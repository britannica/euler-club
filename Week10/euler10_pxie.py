def isPrime(x):
    if x == 1:
        return False
    elif x ==2:
        return True
    else:
        for i in range(2,x):
            if x%i == 0:
                return False
        return True


def firstPrimeList(x):

    result = [];
    for a in range(1,x):
        if isPrime(a):
            result.append(a)
    return result



def findSum():
    exclude = firstPrimeList(1000);
    result = sum(exclude);
    a = list(range(2000))
    new = []
    for y in exclude:
       a = [ x for x in a if x%y != 0]

    print(a);
    for x in a:
        if isPrime(x):
            result+=x
    
   
    return result
            
