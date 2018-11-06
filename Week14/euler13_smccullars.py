# initialize the chain starts'n'counts with the identity 1:1
chain_starts_and_counts = {1:1}

def make_chain(this_chain):
    # the last item in the chain is the current link to check
    link = this_chain[-1]
    # have we seen this chain start before?
    if link in chain_starts_and_counts:
        # we did! process this chain...
        for start in this_chain:
            # the count for start is the how many more entries exist between
            # start's position in this chain and the end of this chain plus
            # the count that we already calculated
            chain_starts_and_counts[start] = len(this_chain) - this_chain.index(start) + chain_starts_and_counts[link]
        return
    elif link % 2 == 0:
        this_chain.append(int(link/2))
    else:
        this_chain.append(3*link+1)
    make_chain(this_chain)

for i in range(1,1000001):
    make_chain([i])

#use the lambda to dynamically fetch the value from each key to pass into max()
print(max(chain_starts_and_counts, key=lambda k: chain_starts_and_counts[k]))
