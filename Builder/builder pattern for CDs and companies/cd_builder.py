from CDType import CDType
from sony import Sony
from samsung import Samsung

# CDBuilder is the factory manager that knows how to build each brand
# concrete builder — it will instantiate the actual product objects and pass them to the base class.
class CDBuilder(CDType):
    def __init__(self):
        sony = Sony()
        samsung = Samsung()
        super().__init__(sony, samsung)
