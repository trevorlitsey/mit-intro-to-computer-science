from lace_strings import laceStrings


def testLaceStrings():
    assert(laceStrings('tomato', 'tomato') == 'ttoommaattoo')
    assert(laceStrings('abc', 'xyz') == 'axbycz')
    assert(laceStrings('abc', 'xyzzz') == 'axbyczzz')
    assert(laceStrings('abcaa', 'xyz') == 'axbyczaa')
