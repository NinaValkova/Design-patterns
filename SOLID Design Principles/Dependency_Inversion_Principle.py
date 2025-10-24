# high level classes or high level modules should not depend directly on low level modules - they should depend on abstraction
# i want to depend on intrfaces rather than concrete implementations

# high level module Research should not depend on concrete implementation - which is Relationship, but sould depend on abstraction that can hange
# high-level module means that uses some other functionality
# low-level module is dealing with things like storage, maybe instead of list it can be used database

from abc import abstractmethod
from enum import Enum


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class Relationships(RelationshipBrowser):
    # relations = []   class-level, shared across all instances
    def __init__(self):
        self.relations = []  # instance-level, unique to each object

    def add_parent_and_child(self, parent, child):
        self.relations.append((parent, Relationship.PARENT, child))
        self.relations.append((child, Relationship.PARENT, parent))

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:
    def __init__(self, browser):
        for p in browser.find_all_children_of("John"):
            print(f"John has a child called {p}")


# class Research:
# dependency on a low-level module directly
# bad because strongly dependent on e.g. storage type

# def __init__(self, relationships):
#     # high-level: find all of john's children
#     relations = relationships.relations - here is dependent on e.g. storage type
#     for r in relations:
#         if r[0].name == 'John' and r[1] == Relationship.PARENT:
#             print(f'John has a child called {r[2].name}.')


parent = Person("John")
child1 = Person("Chris")
child2 = Person("Matt")

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)
