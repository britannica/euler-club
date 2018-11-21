from functools import reduce


def sum_digits(n):
    i = [int(d) for d in str(n)]
    result = reduce(lambda x, y: x+y, i)
    return result


if __name__ == '__main__':
    num = 2**1000
    answer = sum_digits(num)
    print(answer)  # 1366
