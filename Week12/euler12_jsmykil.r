# [1] 76576500
# user     system elapsed 
# 25.645   0.093  25.823 
system.time({
  get.nth.tri.num <- function(n) {
    # create a vector of 1 through n 
    # and then sum them.
    x <- sum(c(1:n))
  }

  get.factor.count <- function(n) {
    b = round(sqrt(n), 0)
    # create a vector of 1 through b
    range <- c(1:b)
    # create a table with the modulus
    # of n and range
    factors <- table(n %% range)
    # count all the results in the table
    # that equal zero and double them
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
