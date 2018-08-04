#from 0 to n the sum of (a+kd) = (n/2)(2a-(n-1)d) where a is starting value, d is interval, and n is number of terms

import time
def calculate(n):
  sum3 = getSeriesSum(3, n)
  sum5 = getSeriesSum(5, n)
  sum15 = getSeriesSum(15, n)
  print (sum3+sum5-sum15)
  return 

def getSeriesSum(val, limit):
  n = int((limit-1)/val)
  x = (n*(2*val+(n-1)*val))/2
  return x

start = time.time()
calculate(1000)
end = time.time()
print(end - start)
