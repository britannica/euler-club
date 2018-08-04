def calculate():
  multiples = set()
  sum = 0
  getMultiplesOf(3, 1000, multiples)
  getMultiplesOf(5, 1000, multiples)
  for val in multiples:
    sum += val
  print (sum)
  return 

def getMultiplesOf(val, limit, multiples):
  x = 0
  while x < limit:
    multiples.add(x)
    x+=val
  return

calculate()
