# if i have some interface that takes some sort of base class
# then any subclass I pass in should be able to replace that base class
# without changing the expected behavior of the interface.


# boolean property on rectagle that telling wheteher or not this is s square
# factory method - that making suare instead of rectangle
class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return self._width * self._height

    def __str__(self):
        return f"Width: {self.width}, height: {self.height}"

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    # boolean property on rectagle that telling wheteher or not this is s square
    @property
    def is_square(self):
        """Return True if the rectangle is actually a square."""
        return self._width == self._height


class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size, size)

    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._width = self._height = value


# def use_it(rc):
#     w = rc.width
#     rc.height = 10  # unpleasant side effect
#     expected = int(w * 10)
#     print(f"Expected an area of {expected}, got {rc.area}")


def use_it(rc):
    """
    Safe version of use_it that handles both Rectangle and Square properly.
    """
    if rc.is_square:
        expected = rc.width * rc.height
        print(f"Expected an area of {expected}, got {rc.area}")

    else:
        w = rc.width
        rc.height = 10  # only safe for rectangles
        expected = int(w * 10)
        print(f"Expected an area of {expected}, got {rc.area}")


rc = Rectangle(2, 3)
use_it(rc)

sq = Square(5)
use_it(sq)
