import copy


class Address:
    def __init__(self, street_address, suite, city) -> None:
        self.city = city
        self.street_address = street_address
        self.suite = suite

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.suite}"


class Employee:
    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} works at {self.address}"


# when we have fixed number of prototypes that we are using in system, we can put them into  factory and makes factory methods - so construction of copies of those prototypes is easier


class EmployeeFactory:
    main_office_employee = Employee("", Address("123 East Dr", 0, "London"))
    aux_office_employee = Employee("", Address("123B East Dr", 0, "London"))

    @staticmethod
    def __new_employee(prototype, name, suite):
        result = copy.deepcopy(prototype)
        result.name = name
        result.address.suite = suite
        return result

    @staticmethod
    def new_main_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.main_office_employee, name, suite
        )

    @staticmethod
    def new_aux_office_employee(name, suite):
        return EmployeeFactory.__new_employee(
            EmployeeFactory.aux_office_employee, name, suite
        )


john = EmployeeFactory.new_aux_office_employee("John", 101)
jane = EmployeeFactory.new_aux_office_employee("Jane", 500)

print(john)
print(jane)
