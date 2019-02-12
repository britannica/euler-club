
find.proper.divisors <- function(number) {
  range <- c(1:number)
  divisors.bool <- number %% range == 0
  divisors <- range[c(divisors.bool)] #from bools to values
  proper.divisors <- head(divisors, -1) #remove the number its self
}

calculate.is.abundant <- function (nums, num) {
  isAbundant <- sum(nums) > num
}

range <- c(1:28123);
# find proper divsors for all numbers under 28123s
divisor.list <- lapply(range, find.proper.divisors) #returns a list
# find all abundant numbers under 28123
abundant.numbers.in.range <- unlist(range[c(mapply(calculate.is.abundant,divisor.list,range))]) #returns a list
# get every sum combination and filter out dupes
# these are all the numbers that abundant sums under 2813 can add up to
sum.combinations <- rowSums(expand.grid(abundant.numbers.in.range, abundant.numbers.in.range))
bool.combinations <- range[c(range %in% sum.combinations)]
print(sum(range[c(! range %in% bool.combinations)]))

