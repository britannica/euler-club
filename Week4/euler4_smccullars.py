def is_palindrome(number):
    midpoint = round(len(str(number)) / 2)
    for i in range(0, midpoint):
        if str(number)[i] != str(number)[-(i+1)]:
            return False
    return True

largest_palindrome = 0

for i in range(100,999):
    for j in range(i,999):
        candidate = i * j
        if candidate > largest_palindrome and is_palindrome(candidate):
            largest_palindrome = candidate

print("largest_palindrome is: ", largest_palindrome)
