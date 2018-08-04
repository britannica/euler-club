import time
def calculate(n):
    sum = 0
    for i in range(1,n):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
    print(sum)
    return 

start = time.time()
calculate(1000)
end = time.time()
print(end - start)
