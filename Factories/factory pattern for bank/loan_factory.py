from typing import Optional
from abstract_factory import AbstractFactory
from loan_type import LoanType 
from home_loan import HomeLoan
from business_loan import BusinessLoan
from education_loan import EducationLoan
from loan import Loan
from bank import Bank

class LoanFactory(AbstractFactory):
    def __init__(self):
        self.loanType = {
            "HOME": LoanType.HOME,
            "BUSINESS": LoanType.BUSINESS,
            "EDUCATION": LoanType.EDUCATION
        }

    def getLoan(self, type) -> Optional[Loan]:
        value = self.loanType.get(type.upper())

        loan = None
        if value == LoanType.HOME:
            loan =  HomeLoan()  
        elif value == LoanType.BUSINESS:
            loan =  BusinessLoan()  
        elif value == LoanType.EDUCATION:
            loan = EducationLoan()

        return loan

    def getBank(self, type) -> Optional[Bank]:
        return None
