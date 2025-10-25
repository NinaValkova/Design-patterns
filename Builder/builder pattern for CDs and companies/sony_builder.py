class SonyBuilder:
    def __init__(self, sony):
        self.sony = sony

    def show_items(self):
        print(f"CD name: {self.sony.pack()}, Price: {self.sony.price()}")
        return self
