from problem1 import Loan


def test_loan():
    """Tests loan"""
    loan1 = Loan(484, 0.2, 0.04)

    for num in range(12):
        loan1.apply_payment()
        loan1.update_monthly_balance()

    result1 = loan1.get_balance()

    assert(result1 == 361.61)

    loan2 = Loan(42, 0.2, 0.04)

    for num in range(12):
        loan2.apply_payment()
        loan2.update_monthly_balance()

    result2 = loan2.get_balance()

    assert(result2 == 31.38)
