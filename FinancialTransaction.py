from datetime import date
from math import exp
today = date.today()
r_free = 0.05/365.0

class FinancialTransaction(object):
    def __init__(self, t, a, description=''):
        self.t = t
        self.a = a
        self.description = description
    def pv(self, t0=today, r=r_free):
        return self.a*exp(r*(t0-self.t).days)
    def __str__(self):
        return '%.2f dollars in %i days (%s)' % (self.a, self.t, self.description)

class CashFlow(object):
    def __init__(self):
        self.transactions = []
    def add(self,transaction):
        self.transactions.append(transaction)
    def pv(self, t0, r=r_free):
        return sum(x.pv(t0, r) for x in self.transactions)
    def __str__(self):
        return '\n'.join(str(x) for x in self.transactions)

bond = CashFlow()
today = date(2016, 1, 1)
for year in range(2016, 2018):
    for month in range(1, 13):
        coupon = FinancialTransaction(date(year, month, 20), 1000)
        bond.add(coupon)
print(round(bond.pv(today, r=0.05/365), 0))
