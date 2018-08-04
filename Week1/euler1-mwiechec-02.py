def calculate():
  multiples3 = getMultiplesOf(3, 1000)
  multiples5 = getMultiplesOf(5, 1000)
  sum = 0
  for val in multiples3 | multiples5:
    sum += val
  print (sum)
  return 

def getMultiplesOf(val, limit):
  multiples = set()
  x = val
  while x < limit:
    multiples.add(x)
    x += val
  return multiples

calculate()
