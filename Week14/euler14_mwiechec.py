import time
import functools


def memoize(func):
    """Wrapper function to cache function results"""
    memo = {}

    @functools.wraps(func)
    def wrapper(key):
        if key in memo:
            return memo[key]
        else:
            memo[key] = func(key)
            return memo[key]
    return wrapper


def timer(func):
    """Wrapper function to time function call"""
    @functools.wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


def collatz_func(x):
    """Collatz function"""
    if x % 2 == 0:
        y = x//2
    else:
        y = (x*3)+1
    return y


# @functools.lru_cache(maxsize=None)
@memoize
def collatz_sequence_length(x):
    """Calculates the length of a Collatz Sequence"""
    y = collatz_func(x)
    if y == 1:
        return 2
    else:
        sequence_length = collatz_sequence_length(y)
        sequence_length += 1
        return sequence_length


@timer
def get_longest_sequence(limit):
    """Finds the longest Collatz Sequence upto a given limit, returns the seed value and length"""
    solution = (0, 1)
    for num in range(1, limit):
        length = collatz_sequence_length(num)
        if solution[1] < length:
            solution = (num, length)
    return solution


if __name__ == '__main__':
    answer = get_longest_sequence(1000000)
    print(answer)
