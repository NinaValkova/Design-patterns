from abc import abstractmethod
from typing import Optional
from loan import Loan
from bank import Bank


class AbstractFactory:
    @abstractmethod
    def getBank(self, type) -> Optional[Bank]:
        pass

    @abstractmethod
    def getLoan(self, type) -> Optional[Loan]:
        pass
