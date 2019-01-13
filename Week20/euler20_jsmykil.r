library(gmp); 
options(scipen = 999)
hundred.factorial = factorialZ(100)
hundred.factorial.vector = as.numeric(strsplit(as.character(hundred.factorial), "")[[1]])
print(sum(hundred.factorial.vector))