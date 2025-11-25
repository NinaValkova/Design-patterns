from abc import abstractmethod, ABC


class Employee(ABC):
    @abstractmethod
    def get_id(self):
        pass
    
    @abstractmethod
    def get_name(self):
        pass
    
    @abstractmethod
    def get_salary(self):
        pass
    
    @abstractmethod
    def print(self):
        pass
    
    @abstractmethod
    def add(self, employee):
        pass
    
    @abstractmethod
    def remove(self, employee):
        pass
    
    @abstractmethod
    def get_child(self, index):
        pass