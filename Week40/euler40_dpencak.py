fract = ''

for i in range(1, 1000001):
  fract += str(i)

fractList = list(fract)

indexes = [0, 9, 99, 999, 9999, 99999, 999999]

result = 1

for index in indexes:
  result *= int(fractList[index])

print(result)