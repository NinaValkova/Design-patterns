# Adaptee - class whose interface DOES NOT match what the client expects
# reuse without modifying it
class BankDetails:
    def __init__(self):
        self.bank_name = ""
        self.acc_holder_name = ""
        self.acc_number = 0
    
    def set_bank_name(self, bank_name):
        self.bank_name = bank_name
        
    def get_bank_name(self):
        return self.bank_name
    
    def set_acc_holder_name(self, acc_holder_name):
        self.acc_holder_name = acc_holder_name

    def get_acc_holder_name(self):
        return self.acc_holder_name

    def set_acc_number(self, acc_number):
        self.acc_number = acc_number

    def get_acc_number(self):
        return self.acc_number
