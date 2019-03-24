# euler29

from collections import defaultdict
import time
t0 = time.time()

# grid_size = 1001
all_terms = defaultdict(dict)

for a in range(2, 101):
    for b in range(2, 101):
        all_terms[a**b] = 1
        
print('terms={0}'.format(len(all_terms)))
 

t1 = time.time()
elapsed = t1 - t0
print('time={0}'.format(elapsed))


-----------------------------
terms=9183
time=0.0160000324249
