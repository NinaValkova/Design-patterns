# The decorator function
# class_ is the class being decorated
def singleton(class_):
    # instances = { Database: <Database object> }
    instances = {}

    def get_instance(*args, **kwargs):
        # creates the instance the first time and afterwards returns the already-created one
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance   


# @singleton
# class Database:

# is equivalent to:

# Database = singleton(Database) - Database now refers to the function get_instance, not the class

@singleton
class Database:
    # initializer does not get called several times
    def __init__(self):
        print('Loading database')

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)
