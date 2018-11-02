from deepreverse import deep_reverse


def test_deep_reverse():
    assert(deep_reverse([[1, 2], [3, 4], [5, 6, 7]])
           == [[7, 6, 5], [4, 3], [2, 1]])
