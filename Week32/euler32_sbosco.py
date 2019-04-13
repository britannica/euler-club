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
        print(multiplicand, multiplier, product)
        good_prods.add(product)
        
    multiplicand = int(i[0]+i[1])
    multiplier = int(i[2]+i[3]+i[4])
    product = int(i[5]+i[6]+i[7]+i[8])
    if multiplicand * multiplier == product:
        print(multiplicand, multiplier, product)
        good_prods.add(product)

total = sum(good_prods)
print('\ntotal={0}'.format(total))



12, 483, 5796
18, 297, 5346
27, 198, 5346
28, 157, 4396
39, 186, 7254
4, 1738, 6952
4, 1963, 7852
42, 138, 5796
48, 159, 7632

total=45228

time=1.81299996376
