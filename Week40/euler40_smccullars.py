champernowne = '0'

for n in range(1, 1000000):
    champernowne += str(n)

answer = 1

for d in range(0, 7):
    answer *= int(champernowne[10**d])

print(answer)
