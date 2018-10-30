from biggest import biggest


def test_biggest():
    assert(biggest({'a': [], 'b': [1, 7, 5, 4, 3, 18, 10, 0]}) == 'b')
