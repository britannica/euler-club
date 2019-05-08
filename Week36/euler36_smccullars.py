def is_palindrome(l):
    for i in range(0, int(len(l)/2)):
        if l[i] != l[-i-1]:
            return False
    return True

palindromes = []

for x in range(1, 1000000):
    if is_palindrome(str(x)) and is_palindrome('{0:b}'.format(x)):
        palindromes.append(x)

print(sum(palindromes))
