# (9**5)*6 = 354294...which is greater than 100000, so
# there can be a sum of fifth digit powers with 6 terms

# (9**5)*7 = 413343...which is less than one million, so
# there cannot be a sum of fifth digit powers with 7 or more terms

total = 0

for i in range(10,1000001):
    # int->string->list of characters
    # then sum the fifth power of each
    s = sum(int(d) ** 5 for d in list(str(i)))
    if s == i:
        total += s

print(total)
