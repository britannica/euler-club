# find the remainder, carry down the zero
def next_step(dividend, divisor):
    return (dividend % divisor) * 10

def long_division(dividend, divisor):
    steps = [next_step(dividend,divisor)]
    while next_step(steps[-1], divisor) not in steps:
        steps.append(next_step(steps[-1], divisor))
    # if our last step returned zero, there is no cycle
    # because the long division process ended successfully
    if steps[-1] == 0:
        return []
    else:
        # the cycle may only be a subset of all steps (ie. 1/6 or 1/76)
        # ignore everything until we find the beginning step
        for index,step in enumerate(steps):
           if step == next_step(steps[-1], divisor):
               return steps[index:]

# Even though there *could* be two cycles of equal length...because
# the problem clearly says there is one unique answer, we can safely
# flip the usual key/value pair (to make sorting easier).  When
# there are multiple cycles of equal length, this approach would
# result in us finding the largest value of i for that cycle count.

cycles = {}
for i in range(2,1000):
#    print('{}: {}'.format(i, long_division(1,i)))
    cycles[len(long_division(1,i))] = i

print(cycles[max(cycles)])
