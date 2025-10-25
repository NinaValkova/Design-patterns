from abc import abstractmethod
from cd import CD

# bridge between CD and concrete products
# Company represents a manufacturer like Sony or Samsung

# ensures that any subclass (like Sony) must define both:
# pack() (from CD)
# price() (from Company)

class Company(CD):
    @abstractmethod
    def price(self):
        pass
