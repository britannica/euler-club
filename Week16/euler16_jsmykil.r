options(scipen=999)

sumExponents <- function(num, exp) {
  expNumber = num^exp
  expNumberAsCharachter = as.character(expNumber)
  expCharachterSplit = strsplit(expNumberAsCharachter, "")
  expCharachterAsNumeric = as.numeric(expCharachterSplit[[1]])
  sum(expCharachterAsNumeric)
}

print (sumExponents(2, 1000))