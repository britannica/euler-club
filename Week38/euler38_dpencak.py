multipliers = [1, 2]
maxPalindrome = 0

for i in range(2, 10001):
    concat = ""
    index = 0

    while len(concat) < 9:
        product = i * multipliers[index]
        concat += str(product)
        multipliers.append(multipliers[len(multipliers) - 1] + 1)
        index += 1
    
    if len(concat) == 9:
        if len(set(concat)) == 9 and "0" not in concat:
            if (int(concat) > maxPalindrome):
                maxPalindrome = int(concat)

print(maxPalindrome)