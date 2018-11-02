from applyfilter import applyF_filterG


def test_apply_filter():
    def f(i):
        return i + 2

    def g(i):
        return i > 5

    L = [0, -10, 5, 6, -4]
    assert(applyF_filterG(L, f, g) == 6)
    assert(L == [5, 6])


def test_apply_filter2():
    def f(i):
        return i - 10

    def g(i):
        return i < -5

    L = [0, -10, 5, 6, -4]
    assert(applyF_filterG(L, f, g) == 0)
    assert(L == [0, -10, -4])
