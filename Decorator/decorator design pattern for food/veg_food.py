from food import Food

class VegFood(Food):
    def prepare_food(self):
        return "Veg Food"
    
    def food_price(self):
        return 50.0