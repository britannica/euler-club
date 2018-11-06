system.time({
highest_chain = 0;

do.collatz <- function(x) {
  ifelse(x %% 2  == 0, x / 2, 3*x + 1)
}

#[1] 524
#[1] 837799
#user   system  elapsed 
#5849.078  199.860 6341.996 

starting_number = 999999
next_number = starting_number

complete_set <- c(1:starting_number)
left_overs <- complete_set
answer <- 0
vector <- c()

while (length(left_overs) > 0) {
  number <- left_overs[length(left_overs)]
  tmpNumber <- number
  vector <- c()
  vector <- c(vector, number)
  while (do.collatz(number) != 1) {
    next_number = do.collatz(number)
    vector <- c(vector, next_number)
    number <- next_number
  }
  
  if (highest_chain < length(vector)) {
    highest_chain = length(vector)
    answer <- tmpNumber
  }
  
  left_overs <- left_overs[!left_overs %in% vector]
}

print(highest_chain)
print(answer)
})


