from typing import Optional
from bank_factory import BankFactory
from loan_factory import LoanFactory
from abstract_factory import AbstractFactory

class FactoryCreator:

    @staticmethod
    def getFactory(choice) -> Optional[AbstractFactory]:
        if choice.upper() == "BANK":
            return BankFactory()
        elif choice.upper() == "LOAN":
            return LoanFactory() 
        
        return None
