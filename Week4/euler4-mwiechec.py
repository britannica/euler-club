def is_palindrome(pstr):
    rstr = pstr[::-1]
    return (rstr == pstr)


answer = 1
p = False
# loop 999 to 100 - only need to do 3 digit numbers
for x in range(999, 100, -1):
    # set inner loop to x because we already checked it
    for y in range(x, 100, -1):
        m = x * y
        p = is_palindrome(str(m))
        if p and (m > answer):  # just get largest palindrome
            answer = m
            
print (answer)
