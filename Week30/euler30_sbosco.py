# euler30

import time
t0 = time.time()

power = 5

def upperlimit(power):
    digits = 1
    while(len(str(9**power*digits)) > digits):
        digits += 1
    return 9**power*digits


maxnum = upperlimit(power)
answer = 0

for x in range(2, maxnum+1):
    total = 0
    digits = list(str(x))
    for digit in digits:
        total += int(digit)**power
    if total == x:
        print("{0}".format(x))
        answer += x       

        
print('sum of terms={0}'.format(answer))
 

t1 = time.time()
elapsed = t1 - t0
print('time={0}'.format(elapsed))


4150
4151
54748
92727
93084
194979
sum of terms=443839
time=1.79200005531
