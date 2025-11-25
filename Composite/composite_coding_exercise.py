from pydantic import InstanceOf


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
                total += item.sum  # item.sum returns the integer
                # item.sum() tries to CALL the integer → error
            elif isinstance(item, SingleValue):
                total += item.sum
            else:
                total += item

        return total


single_value = SingleValue(11)
other_values = ManyValues()
other_values.append(22)
other_values.append(33)
# make a list of all values
all_values = ManyValues()
all_values.append(single_value)
all_values.append(other_values)

# test expects property
print(all_values.sum == 66)
