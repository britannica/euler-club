known_sequences = {1:1}

def next(seq):
    i = seq[-1]
    if i in known_sequences:
        if len(seq) > 1:
            seq.pop()
            #done
            for n in seq:
                known_sequences[n] = len(seq) - seq.index(n) + known_sequences[i]
#        print(seq)
        return known_sequences[seq[0]]
    elif i % 2 == 0:
        seq.append(int(i/2))
    else:
        seq.append(3*i+1)
    return next(seq)

longest_start_number = 0
longest_chain_length = 0
for i in range(1,1000001):
    chain_length = next([i])
    if chain_length > longest_chain_length:
        longest_start_number = i
        longest_chain_length = chain_length
print(longest_start_number)
