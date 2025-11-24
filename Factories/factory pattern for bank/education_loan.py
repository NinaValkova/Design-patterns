from loan import Loan


class EducationLoan(Loan):
    def getInterestRate(self, rate):
        self.rate = rate
