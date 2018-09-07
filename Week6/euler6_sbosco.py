def sumsquares(limit):
    sum = 0
    for x in range(1,limit+1):
        sum += x*x
    return sum
    
def squaresums(limit):
    sum = 0
    for x in range(1,limit+1):
        sum += x
    return sum * sum

def differ(limit):
    sum = sumsquares(limit)
    square = squaresums(limit)
    diff = square - sum
    print(sum, square, diff)
    
differ(100)


