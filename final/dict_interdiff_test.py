from dict_interdiff import dict_interdiff


def test_dict_interdiff():
    d1 = {1: 30, 2: 20, 3: 30, 5: 80}
    d2 = {1: 40, 2: 50, 3: 60, 4: 70, 6: 90}
    assert(dict_interdiff(d1, d2) == (
        {1: 70, 2: 70, 3: 90}, {4: 70, 5: 80, 6: 90}))
