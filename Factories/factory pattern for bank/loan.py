from abc import abstractmethod
import math


class Loan:
    def __init__(self) -> None:
        self.rate = 0.0

    @abstractmethod
    def getInterestRate(self, rate):
        pass    

    def calculateLoanPayment(self, loanAmount, years):
        monthlyInstallments = years * 12
        monthlyRate = self.rate / 1200

        monthlyPayment = (
            (monthlyRate * math.pow((1 + monthlyRate), monthlyInstallments))
            / (math.pow((1 + monthlyRate), monthlyInstallments) - 1)
        ) * loanAmount

        print(f"Your monthly EMI is {monthlyPayment:.1f} for the amount {loanAmount}")
