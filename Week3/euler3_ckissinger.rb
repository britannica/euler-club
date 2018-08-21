# https://projecteuler.net/problem=3
class Euler3
  def self.prime?(num)
    square_root_rounded_down = round_down_square_root(num)
    (2..square_root_rounded_down).each do |possible_factor|
      return false if (num % possible_factor).zero?
    end
    true
  end
  num_to_factor = 600_851_475_143
  primes = []

  def self.round_down_square_root(num_to_factor)
    Math.sqrt(num_to_factor).floor
  end

  square_root_rounded_down = round_down_square_root(num_to_factor)

  (2..square_root_rounded_down).each do |num|
    dividend = num_to_factor / num
    primes.push num if (num_to_factor % num).zero? && prime?(num)
    primes.push dividend if (num_to_factor % dividend).zero? && prime?(dividend)
  end

  print(primes.last)
end