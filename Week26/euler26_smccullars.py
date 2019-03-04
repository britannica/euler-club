class LongDivisionStepper:
    def __init__(self, dividend, divisor):
        self.divisor = divisor
        self.steps = [dividend]

    def step(self):
        # modulus to find the remainder, carry down the zero
        return (self.steps[-1] % self.divisor) * 10

    def cycle(self):
        # as long as the next step is not a repeated step, keep going
        while self.step() not in self.steps:
            self.steps.append(self.step())
        # if the last step returned zero, the division successfully
        # terminated and there is no cycle
        if self.steps[-1] == 0:
            return []
        else:
            # the cycle may only be a subset of all steps (ie. 1/6 
            # or 1/76) ignore everything until we find the beginning
            # step (aka the repeated step)
            repeated_step = self.step()
            for index,step in enumerate(self.steps):
                if step == repeated_step:
                    return self.steps[index:]

# Even though there *could* be two cycles of equal length...because
# the problem clearly says there is one unique answer, we can safely
# flip the usual key/value pair (to make sorting easier).  When
# there are multiple cycles of equal length, this approach would
# result in us finding the largest value of i for that cycle count.
cycles = {}
for i in range(2,1000):
    cycle = LongDivisionStepper(1,i).cycle()
    cycles[len(cycle)] = i
print(cycles[max(cycles)])
