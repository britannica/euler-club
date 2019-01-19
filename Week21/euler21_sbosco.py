# euler21

import math
import time
t0 = time.time()
all_vals = {}
max_num = 10000
num_sum = 0

def divisor_sum(num):
    dsum = 1
    for i in range(2, int(math.sqrt(num))+1):
        if num % i == 0:
            dsum += i
            dsum += num / i
    return dsum

for x in range (1, max_num+1):
    dsum = divisor_sum(x)  
    all_vals[x] = dsum   

for x in all_vals:
    val = all_vals[x]
    if val < max_num and x < val and all_vals[val] == x:
        print('amicable:', x, val)
        num_sum += x + val
    
print('TOTAL=', num_sum)
            
t1 = time.time()
elapsed = t1 - t0
print('time=', elapsed)



amicable: 220 284
amicable: 1184 1210
amicable: 2620 2924
amicable: 5020 5564
amicable: 6232 6368
TOTAL= 31626
time= 0.07485413551330566
