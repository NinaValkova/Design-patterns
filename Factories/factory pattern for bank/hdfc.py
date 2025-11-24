from bank import Bank

class HDFC(Bank):
    def __init__(self):
        self.BNAME = "HDFC BANK"

    def getBankName(self):
        return self.BNAME