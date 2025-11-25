from employee import Employee


class Accountant(Employee):
    def __init__(self, emp_id, name, salary):
        self.id = emp_id
        self.name = name
        self.salary = salary

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_salary(self):
        return self.salary

    def print(self):
        print("-----------")
        print(f"Id = {self.get_id()}")
        print(f"Name = {self.get_name()}")
        print(f"Salary = {self.get_salary()}")
        print("-----------") 

    def add(self, employee: Employee):
        pass

    def remove(self, employee: Employee):
        pass

    def get_child(self, index: int):
        return None
