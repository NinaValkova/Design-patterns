from sony_builder import SonyBuilder
from samsung_builder import SamsungBuilder


# generic builder base, which knows about the products (sony and samsung) and has methods like build_sony_cd() and show_items().
class CDType:
    def __init__(self, sony, samsung):
        self.sony = sony
        self.samsung = samsung

    def build_sony_cd(self):
        return SonyBuilder(self.sony)

    def build_samsung_cd(self):
        return SamsungBuilder(self.samsung)

    def show_items(self):
        print(f"CD name: {self.sony.pack()}, Price: {self.sony.price()}")
        return self
