import time


def timer(func):
    """Wrapper function to time function call"""
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value
    return wrapper_timer


@timer
def get_total_paths(width, height):
    """Finds the total number of paths of a width by height lattice"""
    location = [[] for y in range(0, height + 1)]
    for y in range(0, height + 1):
        for x in range(0, width + 1):
            if y == 0 or x == 0:
                paths = 1
            else:
                paths = location[y-1][x] + location[y][x-1]
            location[y].append(paths)
    return location[y][x]


if __name__ == '__main__':
    answer = get_total_paths(10, 10)
    print(answer)
