# euler 12


def divisor_count(x):
    count=0
    for i in range(1, x + 1):
        if x % i == 0:
            count += 1
    return count

inc = 559
triangle = 156520
count = 0
while count < 500:
    inc += 1
    triangle += inc
    count = divisor_count(triangle)
    if count > 200:
        print(inc, triangle, count)
print(inc, triangle, count)
