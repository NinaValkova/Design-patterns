# Open-closed principle suggest that when you add new functionality, you add it via extension, not via modification
# open for extension, closed for modification(classed should be closed for modification)

from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum): 
    SMALL = 1
    MEDIUM = 2
    LARGE = 3   

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size

# Specification is a class which determines whether or not a particular item satisfies a particular criteria
class Specification:
    def is_satisfied(self, item):
        pass
    
    def __and__(self, other):
        return AndSpecification(self, other) 


class ColorSpecification(Specification):
    def __init__(self, color):
        self.color = color

    def is_satisfied(self, item):
        return item.color == self.color


class SizeSpecification(Specification):
    def __init__(self, size):
        self.size = size

    def is_satisfied(self, item):
        return item.size == self.size

# combinator is structure which combines other structures
class AndSpecification(Specification):
    def __init__(self, *args):
        self.args = args
    
    def is_satisfied(self, item):
        # checks that every single argument is a boolean value of true - if every single specification is satisfies then the combinatr is satisfid
        return all(map(
            lambda spec: spec.is_satisfied(item), self.args
        ))   


# Filter class use these specifications
class Filter:
    def filter(self, items, spec):
        pass

class BetterFilter(Filter):
    def filter(self, items, spec):
        for item in items:
            if spec.is_satisfied(item):
                yield item

if __name__ == '__main__':
    apple = Product('Apple', Color.GREEN, Size.SMALL)
    tree = Product('Tree', Color.GREEN, Size.LARGE)
    house = Product('House', Color.BLUE, Size.LARGE)

    products = [apple, tree, house]

    bf = BetterFilter()
    print("Green products:")

    green = ColorSpecification(Color.GREEN)
    for p in bf.filter(products, green):
        print(f'- {p.name} is green')

    print("Large products:")  
    large = SizeSpecification(Size.LARGE)
    for p in bf.filter(products, large):
        print(f' - {p.name} is large')

    print("Large blue products:")
    blue = ColorSpecification(Color.BLUE)
    # large_and_blue = AndSpecification(large, blue)
    # for p in bf.filter(products, large_and_blue):
    #     print(f' - {p.name} is large and blue')

    # and keyword is not possible to use, but we can use ampersand
    # combine these tw specifications into one
    large_and_blue = large & blue
    for p in bf.filter(products, large_and_blue):
        print(f" - {p.name} is large and blue")
