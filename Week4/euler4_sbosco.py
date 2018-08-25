# euler 4
def ispalindrome(num):
    test = str(num)
    if test == test[::-1]:
        return 1
    return 0
    
def looper():
    for x in range(999,901,-1):
        for y in range(999,901,-1):
            prod = x*y
            if ispalindrome(prod):
                print(prod, x, y)
                return
                
looper()
    