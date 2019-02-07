def isPrime(p):
    i = 2
    while i<p:
        if p%i==0:
           return False
        else:
            i=i+1
    return True


def largePrime(target):
    index = 3
    largest = 0
    while index<=target:
        if isPrime(index):
            largest = index
            index= index+1
        else:    
            index= index +1
    return largest

    
    
