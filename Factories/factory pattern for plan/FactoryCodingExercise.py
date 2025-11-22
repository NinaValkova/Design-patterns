"""
You are given a class called Person . The person has two attributes: id , and name .

Please implement a  PersonFactory that has a non-static  create_person()  method that takes a person's name and return a person initialized with this name and an id.

The id of the person should be set as a 0-based index of the object created. So, the first person the factory makes should have Id=0, second Id=1 and so on.
"""

from enum import auto


class Person:
    def __init__(self, id, name):
        self.id = id
        self.name = name


class PersonFactory:
    # There is 1 factory instance. That instance has 1 attribute: curr_id. Every call updates the same curr_id
    def __init__(self):
        self.curr_id = 0

    def create_person(self, name):
        person = Person(self.curr_id, name)

        self.curr_id += 1
        return person


pf1 = PersonFactory()
pf2 = PersonFactory()

print(pf1.curr_id)  # 0
print(pf2.curr_id)  # 0

pf1.create_person("Alice")
print(pf1.curr_id)  # 1
print(pf2.curr_id)  # 0
