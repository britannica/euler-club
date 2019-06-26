# euler40

import time
t0 = time.time()

digits = ''
x = 0

while len(digits) < 100000:
    x += 1
    digits += str(x)
print('d1      = {}'.format(digits[0]))
print('d10     = {}'.format(digits[9]))
print('d100    = {}'.format(digits[99]))
print('d1000   = {}'.format(digits[999]))
print('d10000  = {}'.format(digits[9999]))
print('d100000 = {}'.format(digits[99999]))
print('\nproduct = {}'.format(int(digits[0])*int(digits[9])*int(digits[99])*int(digits[999])*int(digits[9999])*int(digits[99999])))

t1 = time.time()
elapsed = t1 - t0
print('\ntime={}'.format(elapsed))



#d1      = 1
#d10     = 1
#d100    = 5
#d1000   = 3
#d10000  = 7
#d100000 = 2
#
#product = 210
#
#time=0.0140001773834
