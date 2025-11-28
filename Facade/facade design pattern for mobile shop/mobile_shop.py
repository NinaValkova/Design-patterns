from abc import abstractmethod


class MobileShop:
    @abstractmethod
    def model_no(self):
        pass
    
    @abstractmethod
    def price(self):
        pass