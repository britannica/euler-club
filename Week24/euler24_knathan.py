import itertools 
n = 0
val = itertools.permutations([0,1,2,3,4,5,6,7,8,9])
for i in list(val):
    n += 1 
    if n == 1000000:
        print (i)