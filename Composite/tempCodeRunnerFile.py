
class SingleValue:
    def __init__(self, value):
        self.value = value
    
    @property
    def sum(self):
        return self.value


class ManyValues(list):
    @property
    def sum(self):
        total = 0
        for item in self:
            if isinstance(item, ManyValues):
                total += item.sum
            elif isinstance(item, SingleValue):
                total += item.sum    
            else:
                total += item

        return total             
