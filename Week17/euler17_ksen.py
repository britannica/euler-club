# Euler 17
# This solution works for numbers between 0 and 9999
# extending to larger numbers should be straightforward.
# Note: I am not adding spaces or trying to put the 'and' at the correct location
# as that is not required by the problem.

numbers = {
        0 : '',
        1 : 'one',
        2 : 'two',
        3 : 'three',
        4 : 'four',
        5 : 'five',
        6 : 'six',
        7 : 'seven',
        8 : 'eight',
        9 : 'nine',
        10 : 'ten',
        11 : 'eleven',
        12 : 'twelve',
        13 : 'thirteen',
        14 : 'fourteen',
        15 : 'fifteen',
        16 : 'sixteen',
        17 : 'seventeen',
        18 : 'eighteen',
        19 : 'nineteen',
        20 : 'twenty',
        30 : 'thirty',
        40 : 'forty',
        50 : 'fifty',
        60 : 'sixty',
        70 : 'seventy',
        80 : 'eighty',
        90 : 'ninety'}

def num2word(N):
    numComp = 0
    W = ''
    if N > 999:
        numComp = numComp + 1
        d = N // 1000
        N = N % 1000
        W = numbers[d] + 'thousand'
    if N > 99:
        numComp = numComp + 1
        d = N //100
        N = N % 100
        W = W + numbers[d] + 'hundred'
    if N > 19:
        if W != '':
            numComp = numComp + 1
        d = N // 10
        N = N % 10
        W = W + numbers[d*10]
        if N != 0:
            numComp = numComp + 1
            W = W + numbers[N]
    else:
        if N > 0:
            numComp = numComp + 1
        W = W + numbers[N]       
    if numComp > 1:
        W = W + 'and'    
    return (W)

totalString = ''
for i in range(1001):
    totalString = totalString + num2word(i)

print (totalString)
print (len(totalString))
# answer = 21124
