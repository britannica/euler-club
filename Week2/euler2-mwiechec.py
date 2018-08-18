import time
def fibsumeven(x):
    res1 = 1
    res2 = 1
    evens = 0
    sum = 0
    while sum < 4000000:
        sum = res1 + res2
        res1, res2 = res2, sum
        if (sum % 2 == 0):
            evens += sum 
    return evens

start = time.time()
print (fibsumeven(35))
end = time.time()
print(end - start)
