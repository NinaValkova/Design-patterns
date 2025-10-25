from company import Company


class Samsung(Company):
    def pack(self):
        return "Samsung CD"

    def price(self):
        return 15

    @staticmethod
    def create():
        from cd_builder import CDBuilder

        return CDBuilder()
