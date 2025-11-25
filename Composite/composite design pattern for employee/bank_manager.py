from employee import Employee


class BankManager(Employee):
    def __init__(self, emp_id, name, salary):
        self.id = emp_id
        self.name = name
        self.salary = salary
        self.children = []
    
    def get_id(self):
        return self.id
    
    def get_name(self):
        return self.name
    
    def get_salary(self):
        return self.salary
    
    def add(self, employee):
        self.children.append(employee)
        
    def remove(self, employee):
        if employee in self.children:
            self.children.remove(employee)
    
    def get_child(self, index):
        if 0 <= index < len(self.children):
            return self.children[index]
        return None          
    
    def print(self):
        print("-----------")
        print(f"Id = {self.get_id()}")
        print(f"Name = {self.get_name()}")
        print(f"Salary = {self.get_salary()}")
        print("Employees under this manager:")
        print("-----------")

        for child in self.children:
            child.print()