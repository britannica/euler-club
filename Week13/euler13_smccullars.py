sum = 0

with open('content.txt') as f:
    for fifty_digit_number in f:
        sum += int(fifty_digit_number.strip())

print(str(sum)[0:10])
