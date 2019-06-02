# euler38

import time
t0 = time.time()



for n in range(1,60000):  
    val1 = n * 1
    val2 = n * 2
    val = str(val1) + str(val2)
    for v in range(3,10):
        if len(val) >= 9:
            break
        valn = n * v
        val += str(valn)
    if len(val) == 9:
        if '1' in val and '2' in val and '3' in val and '4' in val and '5' in val and '6' in val and '7' in val and '8' in val and '9' in val:
            print('integer={}, multiplier-{} pandigital-{}'.format(n, v-1, val))

t1 = time.time()
elapsed = t1 - t0
print('\ntime={0}'.format(elapsed))


# integer=1, multiplier-8 pandigital-123456789
# integer=9, multiplier-5 pandigital-918273645
# integer=192, multiplier-3 pandigital-192384576
# integer=219, multiplier-3 pandigital-219438657
# integer=273, multiplier-3 pandigital-273546819
# integer=327, multiplier-3 pandigital-327654981
# integer=6729, multiplier-2 pandigital-672913458
# integer=6792, multiplier-2 pandigital-679213584
# integer=6927, multiplier-2 pandigital-692713854
# integer=7269, multiplier-2 pandigital-726914538
# integer=7293, multiplier-2 pandigital-729314586
# integer=7329, multiplier-2 pandigital-732914658
# integer=7692, multiplier-2 pandigital-769215384
# integer=7923, multiplier-2 pandigital-792315846
# integer=7932, multiplier-2 pandigital-793215864
# integer=9267, multiplier-2 pandigital-926718534
# integer=9273, multiplier-2 pandigital-927318546
# integer=9327, multiplier-2 pandigital-932718654

# time=0.0969998836517
