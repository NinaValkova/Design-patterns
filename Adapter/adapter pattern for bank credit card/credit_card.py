from abc import abstractmethod

# Target interface
class CreditCard:
    @abstractmethod
    def give_bank_details(self):
        pass
    
    @abstractmethod
    def get_credit_card(self):
        pass
