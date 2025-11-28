class Buffer:
    def __init__(self, width=30, height=20):
        self.width=width
        self.height = height
        self.buffer = [' '] * (width*height)
    
    def __getitem__(self, item):
        return self.buffer.__getitem__(item)
    
    def write(self, text):
        self.buffer += text


class Viewport:
    def __init__(self, buffer=Buffer()):
        self.buffer = buffer
        self.offset = 0
        
    # get a character at a particular location
    def get_char_at(self, index):
        return self.buffer[index+self.offset]

    def append(self, text):
        self.buffer.write(text) 

# facade is designed for hide all complexity
# dont have to fiddle with the internal mechanics of the subsystmes which make the Console work
class Console:
    def __init__(self):
        # Creates one buffer (a big text area)
        # local variable inside the method. - disappears after init
        b = Buffer()
        # Creates one viewport looking into it
        self.curret_viewport = Viewport(b)  # instance attribute - stays as long as the object exists

        self.buffers = [b]
        self.viewports = [self.curret_viewport]

    def write(self, text):
        self.curret_viewport.buffer.write(text) 

    def get_char_at(self, index):
        return self.curret_viewport.get_char_at(index)       

if __name__ == '__main__':
    # when create the console, just call the initializer with no arguments, but plenty of other subsistems are coming into play 
    c=Console()
    c.write('Hello')
