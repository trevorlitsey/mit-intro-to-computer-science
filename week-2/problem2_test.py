from problem2 import Loan


def test_loan1():
    """Assert loan test case 1"""
    loan = Loan(3329, 0.2)

    result = loan.get_lowest_payment_rate()

    assert(result == 310)


def test_loan2():
    """Assert loan test case 2"""
    loan = Loan(4773, 0.2)

    result = loan.get_lowest_payment_rate()

    assert(result == 440)


def test_loan3():
    """Assert loan test case 3"""
    loan = Loan(3926, 0.2)

    result = loan.get_lowest_payment_rate()

    assert(result == 360)
