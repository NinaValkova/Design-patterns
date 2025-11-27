from abc import abstractmethod


class Food:
    @abstractmethod
    def prepare_food(self):
        pass
    
    @abstractmethod
    def food_price(self):
        pass