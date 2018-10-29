def is_evenly_divisible(num, count_through=10):
    for count in reversed(range(1, count_through + 1)):
        if num % count != 0:
            return False
    return True


def find_evenly_divisible(limit):
    num = limit
    while not is_evenly_divisible(num, limit):
        num += limit
    return num
