import time


def get_proper_divs(n):
    factors = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            factors.extend([i, n//i])
    result = set(factors)
    return result


def sum_proper_divs(num):
    factors = get_proper_divs(num)
    result = 0
    for factor in factors:
        result = result + factor
    return result


def get_answer():
    results = {}
    for num in range(1,10000):
        spd = sum_proper_divs(num)
        results[num]=spd
    for num in range(1,10000):
        test = results[num]
        if (num == results.get(test)) and (num != test):
            print ("amicable: ", num)

    return


if __name__ == '__main__':
    start = time.time()
    get_answer()
    end = time.time()
    print(end - start)


# amicable:  220
# amicable:  284
# amicable:  1184
# amicable:  1210
# amicable:  2620
# amicable:  2924
# amicable:  5020
# amicable:  5564
# amicable:  6232
# amicable:  6368
# 0.09803342819213867