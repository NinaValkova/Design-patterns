import copy
from prototype import Prototype


class EmployeeRecord(Prototype):
    def __init__(self, id, name, designation, salary, address):
        self.id = id
        self.name = name
        self.designation = designation
        self.salary = salary
        self.address = address

    def getClone(self):
        return copy.deepcopy(self)

    def __str__(self):
        return f"id {self.id}, name: {self.name}, designation:  {self.designation}, salary: {self.salary}, address: {self.address}"
