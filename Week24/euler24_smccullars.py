import itertools

#use the itertools.permutations to do the lexigraphic generate for me, then use enumerate to get the index of the loop
for idx, perm in enumerate(itertools.permutations(range(0,10))):
    # one millionth zero-index is 999999
    if idx == 999999:
        # turn the tuple of integers into a tuple of strings, join concatenates them into a single string
        print(''.join(map(str,perm)))
        break
