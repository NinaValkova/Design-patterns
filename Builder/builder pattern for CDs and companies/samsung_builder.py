class SamsungBuilder:
    def __init__(self, samsung):
        self.samsung = samsung

    def show_items(self):
        print(f"CD name: {self.samsung.pack()}, Price: {self.samsung.price()}")
        return self
