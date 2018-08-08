# https://projecteuler.net/problem=2
class Euler2
  def self.fibonacci(num)
    return 0 if num.zero?
    return 1 if num == 1
    fibonacci(num - 2) + fibonacci(num - 1)
  end

  def self.even?(cur_fibonacci)
    (cur_fibonacci % 2).zero?
  end

  fibonacci_sum = 0
  cur_fibonacci = 0
  index = 0

  while cur_fibonacci <= 4_000_000
    fibonacci_sum += cur_fibonacci if even?(cur_fibonacci)
    index += 1
    cur_fibonacci = fibonacci(index)
  end
  print(fibonacci_sum)
end