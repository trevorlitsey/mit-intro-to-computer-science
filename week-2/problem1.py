"""This script inits a loan"""


class Loan:
    """Loan class"""

    def __init__(self, balance, annual_interest_rate, monthly_payment_rate):
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

    def get_balance(self):
        """Returns balance."""
        return round(self.balance, 2)
