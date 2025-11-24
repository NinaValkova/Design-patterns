from loan import Loan

class BusinessLoan(Loan):
    def getInterestRate(self, rate):
        self.rate = rate
