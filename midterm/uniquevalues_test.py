from uniquevalues import uniqueValues


def test_unique_values():
    assert(uniqueValues({2: 2, 5: 0, 7: 3}) == [2, 5, 7])
    assert(uniqueValues({1: 1, 2: 1, 3: 1}) == [])
    assert(uniqueValues({1: 1, 2: 1, 3: 3}) == [3])
    assert(uniqueValues({1: 1, 3: 2, 6: 0, 7: 0, 8: 4, 10: 0}) == [1, 3, 8])
