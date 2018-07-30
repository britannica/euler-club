# https://projecteuler.net/problem=1
class Euler1
  def self.multiple_of_three_or_five?(num)
    (num % 3).zero? || (num % 5).zero?
  end
  x = 1
  y = 1000
  sum = 0
  while x < y
    sum += x if multiple_of_three_or_five?(x)
    x += 1
  end
  print(sum)
end
