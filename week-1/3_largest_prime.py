def is_prime(num):
    for count in range(2, int(num ** 0.5) + 1):
        if num % count == 0:
            return False
    return True


def is_factor(divide_by, num):
    if num % divide_by == 0:
        return True
    else:
        return False


def get_largest_prime(limit):
    for num in reversed(range(1, int(limit ** 0.5) + 1)):
        if is_factor(num, limit) and is_prime(num):
            return num
    return 0


# result = get_largest_prime(15000000)
result = get_largest_prime(600851475143)
print(result)
