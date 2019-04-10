import time

COINS = [200,100,50,20,10,5,2,1]
equivalents = {1: 1}


def get_answer():
    seed_equivalents()
    print(equivalents[200])
    pass

def seed_equivalents():
    for seed in [2, 5, 10, 20, 50, 100, 200]:
        oneless = possible_equivalents(seed-1)
        solutions = oneless + 1
        equivalents[seed] = solutions
    return

def possible_equivalents(value):
    for coin in COINS:
        if coin <= value:
            solutions = equivalents[coin]
            value = value - coin
            if value == 0:
                return solutions
            change_solutions = possible_equivalents(value)
            solution = change_solutions * solutions
            return solution


if __name__ == '__main__':
    start = time.time()
    get_answer()
    end = time.time()
    print(end - start)