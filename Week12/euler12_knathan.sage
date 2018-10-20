n = 1
sum = 1
while True:
    if len(sum.divisors()) > 500: break
    n += 1
    sum += n

print ("First triangle number to have over five hundred divisors is: %s") %(sum)