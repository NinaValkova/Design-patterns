from cashier import Cashier
from accountant import Accountant
from bank_manager import BankManager

if __name__ == '__main__':
    emp1 = Cashier(101, "Sohan Kumar", 20000.0)
    emp2 = Cashier(102, "Mohan Kumar", 25000.0)
    emp3 = Accountant(103, "Seema Mahiwai", 30000.0)

    manager = BankManager(100, "Ashwani Rajput", 100000.0)
    manager.add(emp1)
    manager.add(emp2)
    manager.add(emp3)
    
    manager.print()
