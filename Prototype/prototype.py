import copy


class Address:
    def __init__(self, street_address, city, country) -> None:
        self.city = city
        self.street_address = street_address
        self.country = country
    
    def __str__(self):
        return f'{self.street_address}, {self.city}, {self.country}'

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address
    
    def __str__(self):
        return f'{self.name} lives at {self.address}'        

# deepcopy performs a recursive copy of all atributes of an object
# copy performs shallow copy - for example john's address copied as a reference and jane refers to same address

john = Person('John', Address('123 London Road', 'London', 'UK'))
# deepcopy - take john prototype and perform deep copy
jane = copy.deepcopy(john)
# shallow copy
# jane = copy.copy(john)

jane.name = 'Jane'
jane.address.street_address = '124 London Road'
print(john, '\n', jane)
