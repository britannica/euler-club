# euler25

import time
t0 = time.time()

digits_wanted = 1000
all_fibs = {}

def fib(n):
#     print n
    global all_fibs
    if all_fibs.get(n): 
#         print 'already:', n, all_fibs.get(n)
        return all_fibs.get(n)
    if n==1 or n==2:
        all_fibs[n] = 1
        return 1
    f = fib(n-1) + fib(n-2)
    all_fibs[n] = f
    return f

done = False
idx = 0
while (not done):
    idx += 1
    f = fib(idx)
    f_len = len(str(f))
    if f_len == digits_wanted:
        print('idx={0}, len={1}'.format(idx, f_len))
        done = True
    

t1 = time.time()
elapsed = t1 - t0
print('time={0}'.format(elapsed))
