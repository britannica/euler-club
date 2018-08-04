# onlineGDB.com
import time
def calculate(n):
  sum = 0
  x = 3
  while (x < n):
    sum += x
    x+=3
  y = 5
  while y <= n:
    sum += y
    y+=5
    if y >= n: break
    sum += y
    y+=10
  print (sum)
  return 

start = time.time()
calculate(1000)
end = time.time()
print(end - start)
