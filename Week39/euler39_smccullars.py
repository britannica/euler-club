from math import sqrt

# assume a ≤ b ≤ c

# given:
#   a^2+b^2=c^2
#   a+b+c=p
#   a ≤ 1, b ≤ 1, c ≤ 1
#   a,b,c are integers
# simplify and solve for b:
#   a^2+b^2=(p-a-b)^2
#   a^2+b^2=p^2-2pa-2pb+a^2+2ab+b^2
#   p^2-2pa=2pb-2ab
#   p^2-2pa=b(2p-2a)
#   b=(p^2-2pa)/2(p-a)

solutions = {}

for p in range(3, 1000):
    for a in range(1, p):
        b = (p**2-(2*p*a))/(2*(p-a))
        if int(b) == b and b > 0 and a <= b:
            c = sqrt(a**2+b**2)
            if a+b+c == p:
                if p in solutions:
                    solutions[p] += 1
                else:
                    solutions[p] =1

max_solution = max(solutions.values())
print([p for p in solutions if solutions[p] == max_solution])
