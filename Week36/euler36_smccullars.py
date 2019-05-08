def is_palindrome(x):
    for y in range(0, int(len(x)/2)):
        if x[y] != x[-1-y]:
            return False
    return True

total = 0

for x in range(1, 1000000):
    if is_palindrome(str(x)) and is_palindrome(str('{0:b}'.format(x))):
        total += x

print(total)
