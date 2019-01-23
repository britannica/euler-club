number = 220
range <- 1:number
divisors <- number %% range == 0
test = data.frame(range, divisors)

number = 0;
for (i in range) {
  if (test[i, 2]) {
    number = number + i
    print(i)
  }
}
print(range[length(divisors)])
print(number - range[length(divisors)])

#31626

print(get.divisors(220))

get.divisors <- function(n) {
  range <- 1:n
  divisors <- n %% range == 0
  frame <- data.frame(range, divisors)
  print(frame)
  get.sum(range, frame)
} 

get.sum(range, frame) {
  print(frame)
  print(range)
  number = 0;
  for (i in range) {
    if (frame[i, 2]) {
      number = number + i
    }
  }
  number
}