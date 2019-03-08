library(gmp)
#print(fibnum(1000))
options(scipen=999)
fib.start <- c(as.bigz(0),as.bigz(1),as.bigz(1))
length = 1
idx = 0
while (length < 1001) {
  curr.num = fib.start[length(fib.start)]
  prev.num = fib.start[length(fib.start) - 1]
  next.num = curr.num + prev.num
  new.sequence = append(fib.start, next.num)
  #print(as.character(next.num))
  length = nchar(as.character(next.num))
  #print(length);
  fib.start = new.sequence
  idx = idx + 1
}

print(idx)


