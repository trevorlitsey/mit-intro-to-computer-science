"""Contains script to init loan"""
import math


def roundup(x):
    return int(math.ceil(x / 10.0)) * 10


class Loan:
    """Inits loan"""

    def __init__(self, balance, annual_interest_rate):
        self.balance = balance
        self.annual_interest_rate = annual_interest_rate

    def get_lowest_payment_rate(self):
        """returnn lowest payment that can be made to pay off balance in 12 months"""
        monthly_base_payment = self.balance / 12

        # would be better as a reduce function
        total_interest_charged = 0
        balance = self.balance
        for num in range(12):
            balance = balance - monthly_base_payment
            monthly_interest = balance * (self.annual_interest_rate / 12)
            total_interest_charged += monthly_interest

        return roundup(monthly_base_payment + total_interest_charged / 12)
