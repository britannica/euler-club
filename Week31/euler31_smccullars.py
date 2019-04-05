desired_total = 200

denominations = (1,2,5,10,20,50,100,200)

def make_change(changes):
    additions = set()
    deletions = set()
    for change in changes:
        current_total = sum(change)
        if current_total < desired_total:
            deletions.add(change)
            for coin in denominations:
                new_total = current_total + coin
                if new_total <= desired_total:
                    new_change = list(change)
                    new_change.append(coin)
                    additions.add(tuple(sorted(new_change)))
    if additions or deletions:
        changes.difference_update(deletions)
        changes.update(additions)
        return make_change(changes)
    else:
        return changes


# convert the tuple of denominations into a set of one-element tuples
initial_changes = {(c,) for c in denominations}

print(len(make_change(initial_changes)))
