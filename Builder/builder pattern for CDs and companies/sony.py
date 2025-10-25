from company import Company

# Sony is a specific product type — it represents exactly one type of CD.
# The builder (CDBuilder) is dedicated to constructing Sony CDs (or CDs in general) in a controlled way.
# When the client calls Sony.create(), they don’t control the builder chain
# — they just start from a specific product type and delegate building to the builder.


# Sony define real behavior.
class Sony(Company):
    def pack(self):
        return "Sony CD"

    def price(self):
        return 20

    # Sony.create() returns a builder - separate object construction from object usage.
    @staticmethod
    def create():
        from cd_builder import CDBuilder

        return CDBuilder()
