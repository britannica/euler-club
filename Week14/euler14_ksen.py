# This version finds the solution in about 8 seconds
# Another change I planned shold have cut the time further, but didn't finmd time to implememt that

import time
size = 1000000
maxlength = 1
b = bytearray(size+1)
for i in range(size):
    b[i] = 1
for n in range(size,0,-1):
    if (b[n] != 0):    
        count = 1
        m = n
        while (n != 1):
            if (n < size):
                b[n] = 0  
            count = count + 1
            if (n % 2 == 0):
                n = n // 2
            else:
                n = 3 * n + 1             
        if count > maxlength:
            maxlength = count
            longest = m            
print (longest)
