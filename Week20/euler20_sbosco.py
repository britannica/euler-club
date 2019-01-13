# euler20

tot = 1
for i in range (1,101):
    tot *= i
digits_str = list(str(tot))
digits_int = list(map(int, digits_str))
digits_sum = sum(digits_int)

print('sum=', digits_sum)


# sum=648
