# Since Singleton inherits from type, it overrides type.__call__
class Singleton(type):
    instances = {}

    # __call__ controls what happens when you "call" something like Database() - This method executes whenever you write: Database()
    def __call__(cls, *args, **kwargs):
        # cls => the class - literally is the class Database
        if cls not in cls.instances:
            cls.instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls.instances[cls]    

# metaclass is the class of a class - metaclass creates classes
# Python will use your custom metaclass Singleton to create the Database class and control how it behaves
class Database(metaclass=Singleton):
    def __init__(self):
        print('Loading database')

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)


# metaclass
# In Python type is the metaclass used by default.
# Every class you create is actually MyClass = type("MyClass", bases, attributes)

# class Database(metaclass=Singleton):
# is
# Database = Singleton("Database", bases, attributes)

# d = Database()
# Python calls Singleton.__call__(Database, ...)

# super().__call__(*args, **kwargs) Python interprets it as super(Singleton, Singleton).__call__ It causes infinite recursion - Singleton.__call__ calls itself again
# super(Singleton, cls).__call__() calls the default class-creation method (type.__call__) → creates the object normally.

# super(Singleton, cls).__call__(*args, **kwargs) calls type.__call__(cls, *args, **kwargs)
