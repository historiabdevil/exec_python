class CashFlow(object):
    def __init__(self):
        self.transactions = []
    def add(self,transaction):
        self.transactions.append(transaction)
    def pv(self, t0, r=r_free):
        return sum(x.pv(t0, r) for x in self.transactions)
    def __str__(self):
        return '\n'.join(str(x) for x in self.transactions)
