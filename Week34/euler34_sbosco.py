# euler34

import time
t0 = time.time()

facs = [0] * 10
facs[0] = 1
facs[1] = 1
facs[2] = 2
facs[3] = 6
facs[4] = 24
facs[5] = 120
facs[6] = 720
facs[7] = 5040
facs[8] = 40320
facs[9] = 362880

upper_limit = 3265920  #9!*9
sumtot = 0

for n in range(3,upper_limit+1):  
    fac_tot = 0
    for digit in ([int(i) for i in str(n)]):
        fac_tot += facs[digit]
        if fac_tot > n:
            break
    if fac_tot == n:
        print('found={0}'.format(n))
        sumtot += n

print('\ntotal={0}'.format(sumtot))

t1 = time.time()
elapsed = t1 - t0
print('\ntime={0}'.format(elapsed))

#found=145
#found=40585
#
#total=40730
#
#time=20.6429998875
