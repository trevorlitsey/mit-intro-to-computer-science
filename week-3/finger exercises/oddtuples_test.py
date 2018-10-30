from oddtuples import odd_tuples


def test_odd_tubles():
    aTuple = (1, 2, 3, 4, 5)
    bTup = odd_tuples(aTuple)
    assert(bTup == (1, 3, 5))
