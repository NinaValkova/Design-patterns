from typing import Optional
from bank_type import BankType
from sbi import SBI
from hdfc import HDFC
from icici import ICICI
from bank import Bank
from abstract_factory import AbstractFactory
from loan import Loan


class BankFactory(AbstractFactory):
    def __init__(self) -> None:
        self.bankTypes = {"HDFC": BankType.HDFC,
                          "ICICI": BankType.ICICI,
                          "SBI": BankType.SBI}

    def getBank(self, type) -> Optional[Bank]:
        value = self.bankTypes.get(type.upper())

        plan = None
        if value == BankType.HDFC:
            plan = HDFC()
        elif value == BankType.ICICI:
            plan = ICICI()
        elif value == BankType.SBI:
            plan = SBI()    

        return plan 

    def getLoan(self, type) -> Optional[Loan]:
        return None   
