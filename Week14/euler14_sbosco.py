# euler14
import time
    
def collatz(val, allcounts):
    count = 1
    in_val = val
    chain = str(val)
    while val > 1:
        if val in allcounts:
            count += allcounts[val]
            allcounts[in_val] = count
#             print(chain)
            return count
        if val % 2 == 0: # if even
            val = int(val / 2)
        else:
            val = 3 * val + 1
        chain = chain + ' -> ' + str(val)
        count += 1
    allcounts[in_val] = count
#     print(chain)
    return count
    
allcounts = {}
maxval = 0
maxcount = 0
t0 = time.time()
for test in range(2,1000000):
# for test in range(837799,837800):
    count = collatz(test, allcounts)
#     print ('count=',count)
    if count > maxcount:
        maxcount = count
        maxval = test
t1 = time.time()
print('val=',maxval, 'count=',maxcount)
elapsed = t1 - t0
print('time=',elapsed)


#### val= 837799 count= 556
#### time= 6.019999980926514
