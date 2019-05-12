# euler36

import time
t0 = time.time()

def ispalindrome(test):
    if test == test[::-1]:
        return 1
    return 0
    
def looper():
    count = 0
    sumpal = 0
    for x in range(1,1000000,2):
        decx = str(x)
        if ispalindrome(decx):
            binx = '{0:b}'.format(x)
            if ispalindrome(binx):
                print('{}, {}').format(x,binx)
                count += 1
                sumpal += x
    print('\ncount={}'.format(count))
    print('sum={}'.format(sumpal))
                
looper()

t1 = time.time()
elapsed = t1 - t0
elapsed = t1 - t0
print('\ntime={0}'.format(elapsed))



#1, 1
#3, 11
#5, 101
#7, 111
#9, 1001
#33, 100001
#99, 1100011
#313, 100111001
#585, 1001001001
#717, 1011001101
#7447, 1110100010111
#9009, 10001100110001
#15351, 11101111110111
#32223, 111110111011111
#39993, 1001110000111001
#53235, 1100111111110011
#53835, 1101001001001011
#73737, 10010000000001001
#585585, 10001110111101110001

#count=19
#sum=872187

#time=0.348999977112
