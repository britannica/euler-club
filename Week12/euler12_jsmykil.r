
system.time({
get.nth.tri.num <- function(n) {
  x <- sum(c(1:n))
}

get.factor.count <- function(n) {
  b = round(sqrt(n), 0)
  range <- c(1:b)
  factors <- table(n %% range)
  factorCount <- (factors[names(factors)==0]) * 2
}

find.number <- function() {
  goal <- 501
  index <- 1
  factorCount <- 0
  while(factorCount < goal ) {
    factorCount <- get.factor.count(get.nth.tri.num(index))
    index <- index+1
  }
  get.nth.tri.num(index-1)
}


print(find.number())
})
