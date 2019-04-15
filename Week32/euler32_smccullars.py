# ------------------------------------------------------
# not a formal proof...more like an informal proof
# ------------------------------------------------------
#
# we know that a != b and b != c and a != c because
# a, b, and c must all be unique.
#
# we also can infer that a > 1 and b > 1 and c > 1
# because any number multiplied by 1 is that number.
# 
# multiplication is associative, so a*b == b*a.
# this means that we need only look at a < b 
#
# finally, we can set 2 ≤ a < 98 and a ≤ b < 9876.
#
# we can prove this for a because if a = 98, 
# b cannot be less than 123 which results in c = 12054 
# (or more for larger values of b).  concatenated 
# together, '9812312054' has 10 digits (which 
# exceeds the length requirement).
#
# we can prove this for b by assuming a = 2.  if
# b = 98765, c = 197530.  concatenated together,
# '298765197530' contains 12 digits.  the smallest
# possible 5 digit value for b (when a == 2) is
# 34567, which yields c = 69134.  concatenated together,
# '23456769134' contains 11 digits.  thus, b must be
# less than 5 digits -- which leaves us with the 
# largest possible 4 digit number (with no repeated
# digits) is 9876.
# 
# we can limit b even further by asking "if a=2, what's
# the maximum value for b, such that a*b=c where the
# concatenation of a,b,c has exactly 9 digits?"  it so
# happens that 2*4987=9974 (which meets the digit length
# requirement) whereas 2*5134=10628 (which does not).

TARGET_LENGTH = 9
MAX_A = 98
MAX_B = 4987

pandigital_products = set()

def has_no_zeros(x):
    return '0' not in str(x)

def all_digits_unique(s):
    all_chars = list(s) if isinstance(s, str) else list(str(s))
    unique_chars = set(all_chars)
    return len(all_chars) == len(unique_chars)

def is_allowed(s):
    return has_no_zeros(s) and all_digits_unique(s)

for a in range(2, MAX_A):
    if is_allowed(a):
        for b in range(a+1, MAX_B):
            if is_allowed(b):
                c = a * b
                if is_allowed(c):
                    possible_pandigital = str(a) + str(b) + str(c)
                    if is_allowed(possible_pandigital) and len(possible_pandigital) == TARGET_LENGTH:
                        pandigital_products.add(c)

print(sum(pandigital_products))
