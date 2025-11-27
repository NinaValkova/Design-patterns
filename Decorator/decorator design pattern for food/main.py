from collections import deque
from veg_food import VegFood
from non_veg_food import NonVegFood
from food_decorator import FoodDecorator
from food import Food
from chinese_food import ChineseFood


def print_choices(choices):
    while choices:
        # Removes and returns an element from the left end of the deque.
        choice = choices.popleft()

        if choice == 1:
            food = VegFood()
            print(food.prepare_food())
            print(food.food_price())
        elif choice == 2:
            # Decorate VegFood with NonVegFood
            
            # food = NonVegFood(Food())  # pass = function with no return → returns None super().prepare_food() → None
            # None + "something" → TypeError
            food = NonVegFood(VegFood())
            print(food.prepare_food())
            print(food.food_price())  
        elif choice == 3:
            # Decorate VegFood with NonVegFood
            food = ChineseFood(VegFood())
            print(food.prepare_food())
            print(food.food_price())       
        else:
            print("Other than these no food available")


def main():
    choices = deque()

    while True:
        print("---Food Menu---")
        print("1. Vegetarian Food")
        print("2. Non-Vegetarian Food")
        print("3. Chinese Food")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 4:
            break

        choices.append(choice)

    print_choices(choices)


if __name__ == "__main__":
    main()
