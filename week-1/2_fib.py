from functools import reduce


def get_fib_numbers(limit):
    nums = [1, 2]
    while nums[len(nums) - 1] + nums[len(nums) - 2] <= limit:
        nums.append(nums[len(nums) - 1] + nums[len(nums) - 2])
    return nums


def fib(limit):
    fibs = get_fib_numbers(limit)
    evens_only = filter(lambda x: x % 2 == 0, fibs)
    evens_only_total = reduce(lambda x, y: x + y, evens_only)
    return evens_only_total
