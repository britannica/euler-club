do_exponent <- function(a,b) {
  a**b
}

a_limit <- 100
b_limit <- 100
a_range <- 2:a_limit;
b_range <- 2:b_limit;

answers <- c(sapply(a_range,do_exponent, b_range))
unique_answers <- unique(answers)
print(length(unique_answers))
# 9183