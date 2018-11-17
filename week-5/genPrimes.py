def isPrime(num):
    for count in range(2, int(num ** 0.5) + 1):
        if num % count == 0:
            return False
    return True


def genPrimes():
    num = 2
    while True:
        if isPrime(num):
            yield num
        num += 1
