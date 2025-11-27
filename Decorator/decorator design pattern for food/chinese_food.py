from food_decorator import FoodDecorator

class ChineseFood(FoodDecorator):
    # If a child class does not define __init__
    # Python automatically uses the parent’s __init__ Python internally calls Python internally calls
    def prepare_food(self):
        return super().prepare_food() + " With Fried Rice and Manchurian"

    def food_price(self):
        return super().food_price() + 65.0
