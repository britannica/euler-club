# euler 37
    
def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif (n % 2 == 0 or n % 3 == 0):
        return False
    i = 5
    while i * i <= n:
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i += 6
    return True
    
sumx = 0
for x in range(11,1000001,2):
    strx = str(x)
    all_prime = True
    for lenx in range(0, len(strx)):
        if all_prime:
            test = int(strx[:lenx+1])
            all_prime = is_prime(test)
        if all_prime:
            test = int(strx[lenx:])
            all_prime = is_prime(test)
    if all_prime:
        print(x)
        sumx += x
print('\nsum={}'.format(sumx))
        
# 23
# 37
# 53
# 73
# 313
# 317
# 373
# 797
# 3137
# 3797
# 739397
# 
# sum=748317
