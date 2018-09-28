###########################################################
#    let's take our two equations
#
# a^2+b^2=c^2 and a+b+c=1000 
#
#    which can be rewritten as
#
# a^2+b^2-c^2=0 and c=1000-a-b 
#
#    which can be joined into one equation by substitution
#
# a^2+b^2-(1000-a-b)^2=0 
#
#    and can solve for b via this series of steps
#
# a^2+b^2-(a^2+2ab-2000a+b^2-2000b+1000000)=0
# a^2+b^2-a^2-2ab+2000a-b^2+2000b-1000000=0
# (a^2-a^2)+(b^2-b^2)-2ab+2000a+2000b-1000000=0
# -2ab+2000a+2000b-1000000=0
# -2b(a-1000)+2000a=1000000
# -2b(a-1000)=2(500000-1000a)
# b(a-1000)=1000a-500000
# b(a-1000)=1000(a-500) 
###########################################################
# b = 1000(a-500)/(a-1000)
###########################################################

def calc_b(a):
    return (1000*(a-500))/(a-1000)

def is_natural_number(x):
    return x == int(x)

def is_pythagorean_triplet(a,b,c):
    return a**2+b**2 == c**2

# if a<b<c and a+b+c=1000, then a < 1000/3

max_possible_value_for_a = int(1000/3)

for a in range(1,max_possible_value_for_a):
    b = calc_b(a)
    if a<b and is_natural_number(b):
        c = 1000-a-b
        if b<c and is_natural_number(c) and is_pythagorean_triplet(a,b,c):
            print('found triplet: ' + str(a) + ' ' + str(int(b)) + ' ' + str(int(c)))
            print('product is: ' + str(int(a*b*c)))
