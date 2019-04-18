def find_nontrivial_shared_digit(a, b):
    for x in str(a):
        for y in str(b):
            if x == y and x != '0':
                return x
    return None

def simplify_fraction(numerator, denominator):
    # check for a common prime factor -- since we are only
    # interested in two digit numbers, we can stop checking
    # when x*n > 99 (where x and n is prime).  if x == 2
    # (aka the smallest prime), n is 47
    for p in (2,3,5,7,11,13,17,19,23,29,31,37,41,43,47):
        if numerator % p == 0 and denominator % p == 0:
            return simplify_fraction(int(numerator/p), int(denominator/p))
    return (numerator, denominator)



curious_fractions = []

# we want all two digit numerators
for numerator in range(10,100):
    # we want a two digit denominator, but it must be larger
    # than the numerator for the fraction to be less than 1
    for denominator in range(numerator+1,100):
        # if the numerator and denominator share no digits
        # we can ignore this fraction
        shared_digit = find_nontrivial_shared_digit(numerator, denominator)
        if shared_digit:
            numerator_without_shared_digit = int(str(numerator).replace(shared_digit, '', 1))
            denominator_without_shared_digit = int(str(denominator).replace(shared_digit, '', 1))
            # prevent divide by zero errors
            if denominator_without_shared_digit != 0:
                simplified_fraction = simplify_fraction(numerator, denominator)
                possibly_same_simplified_fraction = simplify_fraction(numerator_without_shared_digit, denominator_without_shared_digit)
                if simplified_fraction == possibly_same_simplified_fraction:
                    curious_fractions.append(simplified_fraction)

numerator_product = 1
denominator_product = 1

for fraction in curious_fractions:
    numerator_product *= fraction[0]
    denominator_product *= fraction[1]

print(simplify_fraction(numerator_product, denominator_product)[1])

# --------------------------------------
# TLDR
# --------------------------------------
# 16/64 --> 1/4
# 19/95 --> 1/5
# 26/65 --> 2/5
# 49/98 --> 1/2 
#---------------------------------------
# (1*1*2*1)/(2*5*5*4) == 2/200 --> 1/100
