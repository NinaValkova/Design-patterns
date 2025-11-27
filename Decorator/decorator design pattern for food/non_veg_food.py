from food_decorator import FoodDecorator

class NonVegFood(FoodDecorator):
    def prepare_food(self):
        return super().prepare_food() + " With Roasted Chicken and Chicken Curry"
    
    def food_price(self):
        return super().food_price() + 150.0
 