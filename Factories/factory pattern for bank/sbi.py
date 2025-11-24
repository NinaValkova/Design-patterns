from bank import Bank

class SBI(Bank):
    def __init__(self):
        self.BNAME ="SBI BANK" 

    def getBankName(self):
        return self.BNAME
