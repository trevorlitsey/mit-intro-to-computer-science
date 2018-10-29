def is_pal(num):
    string = str(num)
    result = True
    for num in range(0, len(string)):
        if string[num] != string[len(string) - 1 - num]:
            result = False
    return result


def find_largest_pal():
    pals = []
    for num1 in reversed(range(100, 1000)):
        for num2 in reversed(range(100, num1)):
            product = num1 * num2
            if is_pal(product):
                pals.append(product)
    return max(pals)
