# https://projecteuler.net/problem=4
def self.num_digits(num)
  num.to_s.size
end

# power_of_ten is 0 for ones place, 1 for tens place, etc.
def self.place(num, power_of_ten)
  (num % (10**(power_of_ten + 1)) - num % 10**power_of_ten) / 10**power_of_ten
end

def self.palindrome?(num)
  num_digits = self.num_digits(num)
  (0..(num_digits / 2) - 1).each do |index|
    # getting the digit at equal depth from opposite side of number,
    # e.g. hundreds and ones position in 3-digit number,
    # thousands and ones position in 4-digit number,
    # hundreds and tens position in 4-digit number, etc.
    mirrored_digit_one = place(num, index)
    mirrored_digit_two = place(num, num_digits - (index + 1))
    return false if mirrored_digit_one != mirrored_digit_two
  end
  true
end

largest_palindrome = 0
(100..999).each do |num|
  (num..999).each do |other_num|
    product = num * other_num
    if palindrome?(product) && product > largest_palindrome
      largest_palindrome = product
    end
  end
end

print(largest_palindrome)