from loan import Loan


class HomeLoan(Loan):
    def getInterestRate(self, rate):
        self.rate = rate
