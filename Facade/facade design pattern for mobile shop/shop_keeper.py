from mobile_shop_plan import MobileShopPlan
from iphone import Iphone
from samsung import Samsung
from blackberry import Blackberry


# ShopKeeper hides multiple shop implementations behind one interface
# User deals with ShopKeeper, not individual shop objects
# main pattern is Facade, even though object creation is done using a small factory method.
class ShopKeeper:
    # Ensures only one instance ever exists
    _instance = None

    # __new__ is the method that creates an object before __init__ initializes it
    # __new__ → creates memory for the object
    # It makes sure that:
    #     -cannot accidentally create two ShopKeeper objects
    # Singleton is used, because the store manager (ShopKeeper) should be unique
    # don’t want multiple “ShopKeepers” handling different stock
    def __new__(cls):
        if cls._instance is None:
            # create the raw object directly from the base class (object)
            # Every class in Python ultimately inherits from object
            cls._instance = super(ShopKeeper, cls).__new__(cls)
        return cls._instance

    # __init__ → fills in the values
    def __init__(self):
        self.mobile_shop_types = {
            1: MobileShopPlan.IPHONE,
            2: MobileShopPlan.SAMSUNG,
            3: MobileShopPlan.BLACKBERRY,
        }

    # factory method because
    #  - It decides which concrete object to create
    def get_mobile_shop(self, type_id):
        plan = self.mobile_shop_types.get(type_id)

        if plan == MobileShopPlan.IPHONE:
            return Iphone()
        elif plan == MobileShopPlan.SAMSUNG:
            return Samsung()
        elif plan == MobileShopPlan.BLACKBERRY:
            return Blackberry()
        else:
            return None

    # Instead of doing:
    # shop = factory.get_mobile_shop(1)
    # shop.model_no()
    # shop.price()

    # Facade provides a simple interface to a complex subsystem(Iphone, Samsung, Blackberry) i
    def get_function(self, type_id):
        mobile_shop = self.get_mobile_shop(type_id)

        if mobile_shop:
            mobile_shop.model_no()
            mobile_shop.price()

        return mobile_shop


"""
a = ShopKeeper()
b = ShopKeeper()
print(a is b)   # True

Thanks to:
cls._instance = super(ShopKeeper, cls).__new__(cls)

"""
