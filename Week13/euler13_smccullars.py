sum = 0

with open('one_hundred_big_numbers.txt') as the_numbers:
    for fifty_digit_number in the_numbers:
        sum += int(fifty_digit_number.strip())

print(str(sum)[0:10])
