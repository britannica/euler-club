import time
def calculate(n):
  multiples3 = getMultiplesOf(3, n)
  multiples5 = getMultiplesOf(5, n)
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

start = time.time()
calculate(1000)
end = time.time()
print(end - start)
