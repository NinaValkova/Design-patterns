from cmath import cos, sin


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"x {self.x}, y: {self.y}"

class PointFactory:
    def new_cartesian_product(self, x, y):
        return Point(x, y)

    @staticmethod
    def new_polar_point(rho, theta):
        return Point(rho * cos(theta), rho * sin(theta))

factory = PointFactory()
if __name__ == "__main__":
    p = Point(2, 3)
    p2 = factory.new_polar_point(1, 2)
