def next_quotient(x,y):
    return (x*10) % y

def long_division_quotients(x,y):
    partial_quotients = []
    while next_quotient(x,y) not in partial_quotients:
        partial_quotients.append(next_quotient(x,y))
        x = next_quotient(x,y)
    if partial_quotients[-1] == 0:
        return 0
    else:
        return len(partial_quotients)

d = 0
longest_cycle_count = 0
for i in range(1,1000):
    cycle_count = long_division_quotients(1,i)
    if cycle_count > longest_cycle_count:
        longest_cycle_count = cycle_count
        d = i

print(d)
