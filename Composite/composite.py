from networkx import draw

# groups of objects (composites): GraphicObject
class GraphicObject:
    def __init__(self, color=None):
        self.color = color
        self.children = []  # is a list you can call drawing.children.append(Square('Red'))

        self._name = 'Group'

    @property
    def name(self):
        return self._name

    def _print(self, items, depth):
        items.append('*' * depth)
        if self.color:
            items.append(self.color)
        items.append(f'{self.name}\n')
        for child in self.children:  # self.children for drawing = [Red Square, Yellow Circle, group] where first two dont have childres  and second time group has its own children
            # RedSquare._print(items, 1)  no children → loop ends
            # YellowCircle._print(items, 1)  no children → loop ends
            # group._print(items, 1)

            child._print(items, depth + 1)

    def __str__(self):
        items = []
        self._print(items, 0)
        return ''.join(items)        

# individual objects (leaves): Circle, Square
class Circle(GraphicObject):
    @property
    def name(self):
        return 'Circle'                

class Square(GraphicObject):
    @property
    def name(self):
        return 'Square'  

# composite design pattern
# making sure that the GraphicObject gets to pretend as being either a scalar base class for something like a circle or a sqare
# or collection by keeping a se of children and then printing those children

if __name__ == '__main__':
    drawing = GraphicObject()
    drawing._name = 'My Drawing'
    drawing.children.append(Square('Red'))
    drawing.children.append(Circle('Yellow'))

    group = GraphicObject()
    group.children.append(Circle('Blue'))
    group.children.append(Square('Blue'))
    drawing.children.append(group)

    print(drawing)

# hierarchy:
# drawing (GraphicObject, name="My Drawing")
# ├── Square('Red')
# ├── Circle('Yellow')
# └── group (GraphicObject, name="Group")
#       ├── Circle('Blue')
#       └── Square('Blue')
