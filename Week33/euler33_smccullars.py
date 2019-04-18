class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __str__(self):
        return '{}/{}'.format(self.numerator, self.denominator)

    def simplify(self):
        # check for a common prime factor -- since we are only interested in two digit numbers, 
        # we can stop checking when x * n > 99 (where x and n is prime).  if x == 2 (aka the 
        # smallest prime), n cannot be more than 47.
        for p in (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47):
            if self.numerator % p == 0 and self.denominator % p == 0:
                simpler_fraction = Fraction(int(self.numerator/p), int(self.denominator/p))
                return simpler_fraction.simplify()
        return self

    # bad simplification means "transform the fraction's numerator and denominator into strings,
    # find a shared digit, remove the shared digit from those strings, and then use those strings
    # to make a new fraction"
    def bad_simplify(self):
        for x in str(self.numerator):
            for y in str(self.denominator):
                if x == y and x != '0':
                    digit_cancelled_numerator = int(str(self.numerator).replace(x, '', 1))
                    digit_cancelled_denominator = int(str(self.denominator).replace(x, '', 1))
                    return Fraction(digit_cancelled_numerator, digit_cancelled_denominator)
        return None


curious_fractions = []

# we want all two digit numerators
for numerator in range(10, 100):
    # we want a two digit denominator, but it must be larger than the numerator for the 
    # fraction to be less than 1
    for denominator in range(numerator+1, 100):
        raw_fraction = Fraction(numerator, denominator)
        mangled_fraction = raw_fraction.bad_simplify()
        # prevent divide by zero errors
        if mangled_fraction and mangled_fraction.denominator != 0:
            if raw_fraction.simplify() == mangled_fraction.simplify():
                    curious_fractions.append(raw_fraction)

numerator_product = 1
denominator_product = 1

for fraction in curious_fractions:
    numerator_product *= fraction.numerator
    denominator_product *= fraction.denominator

solution_fraction = Fraction(numerator_product, denominator_product)

print(solution_fraction.simplify().denominator)

# --------------------------------------
# TLDR
# --------------------------------------
# raw   --> mangled --> simplified
# 16/64 -->   1/4   -->   1/4
# 19/95 -->   1/5   -->   1/5
# 26/65 -->   2/5   -->   2/5
# 49/98 -->   4/8   -->   1/2 
#---------------------------------------
# (1*1*2*1)/(2*5*5*4) == 2/200 --> 1/100
