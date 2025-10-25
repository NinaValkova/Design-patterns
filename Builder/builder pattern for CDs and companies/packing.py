from abc import abstractmethod

# declares what every product must provide pack() and price()

class Packing:

    @abstractmethod
    def pack(self):
        pass

    @abstractmethod
    def price(self):
        pass
