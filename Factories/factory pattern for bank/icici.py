from bank import Bank

class ICICI(Bank):
    def __init__(self):
        self.BNAME = "ICICI BANK"
    
    def getBankName(self):
        return self.BNAME  
