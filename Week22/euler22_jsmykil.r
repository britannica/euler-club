names <- scan("p022_names.txt", what= "", sep=",", na.strings="")
names.sorted <- sort(names)

calculate.score <- function(name, index) {
  print(name)
  name.vector <- unlist(strsplit(name, ""))
  name.letter.indexes <- c(match(name.vector, LETTERS))
  name.letter.sum <- sum(name.letter.indexes)
  name.product <- name.letter.sum * index
}

index = 1
total = 0
for (name in names.sorted) {
  print(name)
  total.count = sum(sum + calculate.score(name, index));
  total = total + total.count
  index = index + 1
}

print(total)
