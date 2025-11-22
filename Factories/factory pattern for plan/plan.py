from abc import abstractmethod


class Plan:
    def __init__(self):
        self.rate = 0.0
    
    @abstractmethod
    def getRate(self) -> None:
        pass
    
    def calculateBill(self, units):
        print(units * self.rate)