from food import Food

class FoodDecorator(Food):
    def __init__(self, new_food):
        self.new_food = new_food

    def prepare_food(self):
        return self.new_food.prepare_food()
    
    def food_price(self):
        return self.new_food.food_price()
