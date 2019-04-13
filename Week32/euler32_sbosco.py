# euler32

import time
t0 = time.time()
from itertools import permutations 

perm = permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 9) 
good_prods = set()
  
for i in list(perm): 
    multiplicand = int(i[0])
    multiplier = int(i[1]+i[2]+i[3]+i[4])
    product = int(i[5]+i[6]+i[7]+i[8])
    if multiplicand * multiplier == product:
        print "{0} x {1} = {2}".format(multiplicand, multiplier, product)
        good_prods.add(product)
        
    multiplicand = int(i[0]+i[1])
    multiplier = int(i[2]+i[3]+i[4])
    product = int(i[5]+i[6]+i[7]+i[8])
    if multiplicand * multiplier == product:
        print "{0} x {1} = {2}".format(multiplicand, multiplier, product)
        good_prods.add(product)

total = sum(good_prods)
print('\ntotal={0}'.format(total))
 

t1 = time.time()
elapsed = t1 - t0
print('\ntime={0}'.format(elapsed))




# 12 x 483 = 5796
# 18 x 297 = 5346
# 27 x 198 = 5346
# 28 x 157 = 4396
# 39 x 186 = 7254
# 4 x 1738 = 6952
# 4 x 1963 = 7852
# 42 x 138 = 5796
# 48 x 159 = 7632
# 
# total=45228
# 
# time=1.83899998665
