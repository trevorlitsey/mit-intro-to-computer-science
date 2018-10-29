"""This script inits a loan"""
import math


class Loan:
    """Loan class"""

    def __init__(self, balance, annual_interest_rate, monthly_payment_rate=None):
        self.balance = balance
        self.annual_interest_rate = annual_interest_rate
        self.monthly_payment_rate = monthly_payment_rate

    def apply_payment(self, payment=None):
        """Applies payment. Returns balance."""
        if payment is None:
            payment = self.balance * self.monthly_payment_rate
        self.balance = self.balance - payment
        return self.balance

    def update_monthly_balance(self):
        """Applies interest expense. Returns balance."""
        self.balance = self.balance + self.balance * \
            (self.annual_interest_rate / 12)
        return self.balance

    def apply_year_of_payments(self, monthly_payment_rate):
        for num in range(12):
            self.apply_payment(monthly_payment_rate)
            self.update_monthly_balance()
        return self.balance

    def find_lowest_payment_rate(self, monthly_payment_rate=None):
        if monthly_payment_rate is None:
            monthly_payment_rate = self.balance / 12
        loan = Loan(self.balance, self.annual_interest_rate,
                    monthly_payment_rate)
        loan.apply_year_of_payments(monthly_payment_rate)
        balance = round(loan.balance, 2)
        if balance == 0.00:
            return math.ceil(monthly_payment_rate * 100) / 100
        elif balance == 0.01:
            return math.ceil(monthly_payment_rate * 100) / 100
        else:
            if balance > 0:
                upper_balance = (
                    (balance * (1 + self.annual_interest_rate / 12)**12) / 12) * 1
                return self.find_lowest_payment_rate(monthly_payment_rate + (upper_balance / 12 / 2))
            else:
                return self.find_lowest_payment_rate(monthly_payment_rate - (balance / 12 / 2))

    def get_balance(self):
        """Returns balance."""
        return round(self.balance, 2)
