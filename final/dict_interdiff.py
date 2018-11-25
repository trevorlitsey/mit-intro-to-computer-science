def f(a, b):
    return a + b


def dict_interdiff(d1={}, d2={}):
    """
    d1 and d2 are dictionaries

    Returns a tuple of two dictionaries:
    a dictionary of the intersect of d1 and d2 and 
    a dictionary of the difference of d1 and d2

    Intersect values == f(d1.2, d2.2)
    """
    d1_keys = d1.keys()
    d2_keys = d2.keys()

    common_dict = {}
    unique_dict = {}

    for key in d1_keys:
        if key in d2_keys:
            common_dict[key] = f(d1[key], d2[key])
        else:
            unique_dict[key] = d1[key]

    for key in d2_keys:
        if key in d1_keys:
            common_dict[key] = f(d1[key], d2[key])
        else:
            unique_dict[key] = d2[key]

    return tuple([common_dict, unique_dict])
