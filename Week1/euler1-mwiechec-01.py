# https://trinket.io/features/python3
def calculate():
  sum = 0
  x = 3
  while (x < 1000):
    sum += x
    x+=3
  y = 5
  while y <= 1000:
    sum += y
    y+=5
    if y >= 1000: break
    sum += y
    y+=10
  print (sum)
  return 

calculate()
