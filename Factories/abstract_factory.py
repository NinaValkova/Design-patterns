from abc import ABC, abstractmethod
from enum import Enum, auto
from typing import Optional


class HotDrink(ABC):

    @abstractmethod
    def consume(self) -> None:
        pass


class Tea(HotDrink):
    def consume(self) -> None:
        print("This tea is delicious")


class Coffee(HotDrink):
    def consume(self) -> None:
        print("This coffee is delicious")


# reference to an abstract base class for the factories - optional for Python, but tells what kind of API is expected
class HotDrinkFactory(ABC):
    @abstractmethod
    def prepare(self, amount) -> HotDrink:
        pass


class TeaFactory(HotDrinkFactory):
    def prepare(self, amount) -> Tea:
        print(f"Put in tea bag, boil water, pour {amount}ml, enjoy!")
        return Tea()


class CoffeeFactory(HotDrinkFactory):

    def prepare(self, amount) -> Coffee:
        print(f"Grind some beans, boil water, pour {amount}ml, enjoy!")
        return Coffee()


# def make_drink(type) -> Optional[HotDrink]:
#     if type == 'tea':
#         return TeaFactory().prepare(200)
#     elif type == 'coffee':
#         return CoffeeFactor().prepare(50)
#     else:
#         return None


class HotDrinkMachine:
    class AvailableDrink(Enum):
        # auto() just assigns automatic integer values.
        # COFFEE → 1
        # TEA    → 2
        COFFEE = auto()
        TEA = auto()

    factories = []  # list that will store tuples (name, factory_instance)
    initialized = False  # prevents running initialization twice - factories are only created once even if you create 10 machines

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                # name = d.name[0] + d.name[1:].lower()
                name = d.name.capitalize()  # "COFFEE" → "Coffee" "TEA" → "Tea"
                factory_name = name + "Factory"
                factory_instance = eval(
                    factory_name
                )()  # gives you the class object CoffeeFactory. Then () creates an instance.
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print("Availble drinks:")
        for f in self.factories:
            print(f[0])

        s = input(f"Please pick drink (0-{len(self.factories)-1})): ")
        idx = int(s)
        s = input(f"Specify amount: ")
        amount = int(s)
        return self.factories[idx][1].prepare(amount)


# Instead of eval, we use a SAFE dictionary
# def __init__(self):
#     self.factories = {
#         "Coffee": CoffeeFactory(),
#         "Tea": TeaFactory(),
#     }

# def make_drink(self):

#     names = list(self.factories.keys())
#     for i, name in enumerate(names):
#         print(f"{i}: {name}")

#     index = int(input(f"Please pick drink (0-{len(names)-1}): "))
#     amount = int(input("Specify amount: "))

#     drink = self.factories[names[index]].prepare(amount)
#     return drink


if __name__ == "__main__":
    # entry = input('What kind of drink would you like?')
    # drink = make_drink(entry)
    # if drink:
    #     drink.consume()
    # else:
    #     print("Unknown drink type!")
    hdm = HotDrinkMachine()
    hdm.make_drink()
