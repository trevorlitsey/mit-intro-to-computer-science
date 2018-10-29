from functools import reduce


def is_multiple(num):
    if num % 3 == 0 or num % 5 == 0:
        return num


def add(x, y):
    return x + y if y else x


sum = reduce(add, map(is_multiple, range(0, 1000)))

print(sum)
