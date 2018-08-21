# https://projecteuler.net/problem=3
class Euler3
  def self.prime?(num)
    square_root_rounded_down = round_down_square_root(num)
    (2..square_root_rounded_down).each { |possible_factor|
      return false if (num % possible_factor).zero?
    }
    true
  end
  num_to_factor = 600_851_475_143
  primes = []

  def self.round_down_square_root(num_to_factor)
    Math.sqrt(num_to_factor).floor
  end

  square_root_rounded_down = round_down_square_root(num_to_factor)

  (2..square_root_rounded_down).each { |num|
    next unless prime?(num)
    primes.push num if (num_to_factor % num).zero?
  }

  print(primes.last)
end