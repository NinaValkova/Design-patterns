from abc import ABC, abstractmethod


#bridge patttern escape complexity explosion as you get more combinations of different classes
#bridge pattern connects two hierarchies of different classes with a parameter
class Renderer(ABC):
    @abstractmethod
    def render_circle(self, radius):
        pass

class VectorRenderer(Renderer):
    def render_circle(self, radius):
        print(f'Drawing a circle of radius {radius}')    


class RasterRenderer(Renderer):
    def render_circle(self, radius):
        print(f"Drawing pixels for a circle of radius {radius}")

class Shape:
    # construct the bridge
    def __init__(self, renderer):
        self.renderer = renderer

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def resize(self, factor):
        pass    

class Circle(Shape):
    def __init__(self, renderer, radius):
        super().__init__(renderer)
        self.radius = radius
      
    # use the bridge to mak the connection to the renderer and draw something    
    def draw(self):
        self.renderer.render_circle(self.radius)
    
    def resize(self, factor):
        self.radius *= factor     

if __name__ == '__main__':
    raster = RasterRenderer()
    vector = VectorRenderer()
    circle = Circle(raster, 5) 
    circle.draw()
    circle.resize(2)
    circle.draw()
