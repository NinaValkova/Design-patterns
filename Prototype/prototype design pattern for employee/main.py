from employeeRecord import EmployeeRecord


def main():
    id = int(input("Enter employee id: "))
    name = input("Enter employee name: ")
    designation = input("Enter employee designation: ")
    salary = float(input("Enter employee salary: "))
    address = input("Enter employee address: ")
    
    employee = EmployeeRecord( id, name, designation, salary, address)
    
    cloned = employee.getClone()
    
    print(cloned)


if __name__ == "__main__":
    main()
