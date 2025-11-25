class Point:
    def __init__(self, x, y):
        self.y = y
        self.x = x


# “drawing” API. - draw_point works only with points, not lines
def draw_point(p):
    print(".", end="")


class Line:
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Rectangle(list):
    def __init__(self, x, y, width, height):
        super().__init__()
        # Rectangle is a list of 4 Line objects, each representing one side
        self.append(Line(Point(x, y), Point(x + width, y)))
        self.append(Line(Point(x + width, y), Point(x + width, y + height)))
        self.append(Line(Point(x, y), Point(x, y + height)))
        self.append(Line(Point(x, y + height), Point(x + width, y + height)))


# when API does not match what actually working with, you need to build in-between component called adapter - in this case adapt line to a point

# Line → sequence of Points
# LineToPointAdapter is a list of Point objects


# using catch reduce temporaries which are generated when implementing the adapter design pattern
# class LineToPointAdapter(list):
class LineToPointAdapter:
    # _count = 0
    cache = {}

    # self.cache = {12345678: [Point(1, 1), Point(1, 2), Point(1, 3)]}

    def __init__(self, line):
        super().__init__()
        # LineToPointAdapter._count += 1

        # The hash value uniquely identifies the line object
        self.h = hash(line)
        if self.h in self.cache:
            # Just reuse the cached list
            return

        print(
            f"Generating points for line "
            f"[{line.start.x}, {line.start.y}]->"
            f"[{line.end.x}, {line.end.y}]"
        )

        # line can be defined in ANY direction.
        # left to right: Point(1, 1) → Point(10, 1) Both represent the same line!
        # right to left: Point(10, 1) → Point(1, 1) Both represent the same line!

        # This normalizes coordinates.
        left = min(line.start.x, line.end.x)  # left = min(1, 10) → 1
        right = max(line.start.x, line.end.x)  # right = max(1, 10) → 10
        top = min(line.start.y, line.end.y)
        bottom = min(line.start.y, line.end.y)

        points = []
        # Vertical line: same x, different y. (5, 1) → (5, 10)
        if right - left == 0:
            for y in range(top, bottom):
                # self.append(Point(left, y))
                points.append(Point(left, y))
        elif line.end.y - line.start.y == 0:
            for x in range(left, right):
                # self.append(Point(x, top))
                points.append(Point(x, top))

        # Store points in the cache
        self.cache[self.h] = points

    # iterating over cached points, not regenerating them
    def __iter__(self):
        # give this iterator to the for loop
        return iter(
            self.cache[self.h]
        )  # iterator iter() is an object Python can call next() on, repeatedly - convert that list into an iterator


def draw(rcs):
    for rc in rcs:
        for line in rc:
            adapter = LineToPointAdapter(line)
            for p in adapter:
                draw_point(p)
            # internally translates this into: iterator = adapter.__iter__()


if __name__ == "__main__":
    rcs = [Rectangle(1, 1, 10, 10), Rectangle(3, 3, 6, 6)]
    draw(rcs)
