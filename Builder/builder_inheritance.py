# never have to go back into person builder and modify it
# if i want additional builders i am using inheritance whihch are open for extension through inheritance but closed for modification


from abc import abstractmethod


class Person:
    def __init__(self):
        self.name = None
        self.position = None
        self.date_of_birth = None

    def __str__(self):
        return f'{self.name} born on {self.date_of_birth} works as a {self.position}'  


class IPersonBuilder:
    @property
    @abstractmethod
    def person(self) -> Person:  # Tell PyLance this returns a Person
        pass

    @abstractmethod
    def build(self):
        pass


# PersonBuilder is generic — it doesn’t belong to a specific type - explicitly controlling the builder chain.
# Tight coupling between builders - each builder depends on an abstract builder
class PersonBuilder(IPersonBuilder):
    def __init__(self):
        self._person = Person()
    
    @property
    def person(self):
        return self._person    

    def build(self):
        return self.person


# class PersonInfoBuilder(PersonBuilder):
#     def called(self, name):
#         self.person.name = name
#         return self

# class PersonJobBuilder(PersonInfoBuilder):
#     def works_as_a(self, position):
#         self.person.position = position
#         return self

# class PersonBirthDateBuilder(PersonJobBuilder):

# # Here’s what Python does under the hood:

# # PersonBirthDateBuilder.__init__() is called.
# # But since you didn’t override __init__ inside PersonBirthDateBuilder,
# # Python looks up the class hierarchy.
# # It finds __init__ in the parent PersonJobBuilder — also missing.
# # It keeps climbing: PersonInfoBuilder? Missing too.
# # Finally, it reaches PersonBuilder.__init__():

#     def born(self, date_of_birth):
#         self.person.date_of_birth = date_of_birth
#         return self


# ------------------------------
# Person info builder (depends on abstraction)
# ------------------------------
class PersonInfoBuilder(IPersonBuilder):
    def __init__(self, builder: IPersonBuilder):
        self.builder = builder

    def called(self, name):
        self.builder.person.name = name
        return self

    def build(self):
        return self.builder.build()


# ------------------------------
# Person job builder (depends on abstraction)
# ------------------------------
class PersonJobBuilder(IPersonBuilder):
    def __init__(self, builder: IPersonBuilder):
        self.builder = builder

    def works_as_a(self, position):
        self.builder.person.position = position
        return self

    def build(self):
        return self.builder.build()


# ------------------------------
# Person birth date builder (depends on abstraction)
# ------------------------------
class PersonBirthDateBuilder(IPersonBuilder):
    def __init__(self, builder: IPersonBuilder):
        self.builder = builder

    def born(self, date_of_birth):
        self.builder.person.date_of_birth = date_of_birth
        return self

    def build(self):
        return self.builder.build()


if __name__ == '__main__':
    # pb = PersonBirthDateBuilder()
    # me = pb\
    #     .called('Dmitri')\
    #     .works_as_a('quant')\
    #     .born('1/1/1980')\
    #     .build()
    # print(me)

    pb = PersonBuilder()

    PersonInfoBuilder(pb).called("Dmitri")
    PersonJobBuilder(pb).works_as_a("Quant")
    PersonBirthDateBuilder(pb).born("1/1/1980")

    # At the end, get the person
    person = pb.build()
    print(person)
