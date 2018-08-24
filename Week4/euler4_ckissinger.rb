# https://projecteuler.net/problem=4
def self.num_digits(num)
  num.to_s.size
end

# place is 1 for ones place, 10 for tens place, etc.
def self.place(num, place)
  (num % (place * 10) - num % place) / place
end

def self.palindrome?(num)
  places = [1, 10, 100, 1000, 10_000, 100_000]
  num_digits = self.num_digits(num)
  places_slice = places[0, num_digits]
  (0..(num_digits / 2) - 1).each do |index|
    # getting the digit at equal depth from opposite side of number,
    # e.g. hundreds and ones position in 3-digit number,
    # thousands and ones position in 4-digit number,
    # hundreds and tens position in 4-digit number, etc.
    mirrored_digit_one = place(num, places_slice[index])
    mirrored_digit_two = place(num, places_slice[-(index + 1)])
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