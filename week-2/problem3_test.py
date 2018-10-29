from problem3 import Loan


def test_loan1():
    """Assert loan test case 1"""
    loan = Loan(320000, 0.2)

    result = loan.find_lowest_payment_rate()

    assert(result == 29157.09)


def test_loan2():
    """Assert loan test case 2"""
    loan = Loan(999999, 0.18)

    result = loan.find_lowest_payment_rate()

    assert(result == 90325.03)
