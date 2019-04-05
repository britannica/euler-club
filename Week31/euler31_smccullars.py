desired_total = 200
denominations = (1,2,5,10,20,50,100,200)

def resolve(solutions):
    additions = set()
    deletions = set()
    for solution in solutions:
        current_total = sum(solution)
        if current_total < desired_total:
            deletions.add(solution)
            for coin in denominations:
                # performance optimization: this ensures that
                # our solution tuples are always in ascending
                # order...which guarantees uniqueness
                if coin >= solution[-1]:
                    if current_total + coin <= desired_total:
                        additions.add(solution + (coin,))
    if additions or deletions:
        solutions.difference_update(deletions)
        solutions.update(additions)
        return resolve(solutions)
    else:
        return solutions

# convert the tuple of denominations into a set of one-element tuples
one_coin_solutions = {(c,) for c in denominations}
print(len(resolve(one_coin_solutions)))
