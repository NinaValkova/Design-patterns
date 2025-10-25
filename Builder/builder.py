# faceted builder pattern
# make two separate builders - one for job information and other for address

class Person:
    def __init__(self):
        self.street_address = None
        self.postcode = None
        self.city = None
        
        self.company_name = None
        self.position = None
        self.annual_income = None
    
    def __str__(self):
        return f'Address: {self.street_address}, {self.position}, {self.city} ' + \
               f'Employed at {self.company_name} as a {self.postcode} earning {self.annual_income}'    

# base class that jumping from one builder to another
class PersonBuilder:
    # person=Person() allow the sub builders to work with an object that's already constructed rather than creating new persons
    # person have been provided from super().__init__(person)
    def __init__(self, person=Person()):
        self.person = person

    def build(self):
        return self.person

    # when work with sub builders i must provide instance that's already been constructed
    # usef for jump one into another
    @property
    def works(self):
        return PersonJobBuilder(self.person)
    
    @property
    def lives(self):
        return PersonAddressBuilder(self.person)

class PersonJobBuilder(PersonBuilder):
    # we pass a person that we're already working on
    def __init__(self, person):
        super().__init__(person) 
    
    def at(self, company_name):
        self.person.company_name = company_name
        return self   
    
    def as_a(self, position):
        self.person.position = position
        return self
    
    def earning(self, annual_income):
        self.person.annual_income = annual_income
        return self

class PersonAddressBuilder(PersonBuilder):
    def __init__(self, person):
        super().__init__(person)

    def at(self, street_address):
        self.person.street_address = street_address
        return self

    def with_postcode(self, postcode):
        self.person.postcode = postcode
        return self

    def in_city(self, city):
        self.person.city = city
        return self        

# pb has a reference to that Person - person=Person()
pb = PersonBuilder()
# When you access .lives property lives(self) is executed
# It creates a new PersonAddressBuilder, and passes in the same Person instance from the base builder
# The chain .at(...).in_city(...).with_postcode(...) Mutate the same shared Person object
person = pb.lives.at("123 London Street").in_city("London").with_postcode("SW12BC")\
         .works.at("Fabrikam").as_a("Engineer").earning(123000)\
         .build()


print(person)


# PersonBuilder acts as a gateway (or facade) that lets you move — or jump — between two specialized builders
# PersonAddressBuilder — for address-related properties
# PersonJobBuilder — for job-related properties
# Both builders operate on the same Person instance, but each is responsible for only one “facet” (or aspect) of the object.


# but every time you add one, you must open PersonBuilder and add a new property (.lives, .works, .studies, .healthy, .socializes, etc.).
# This makes PersonBuilder a central change point — tightly coupling all sub-builders to it.
# Faceted Builder pattern as shown breaks the Open–Closed Principle (OCP)
