class Apple:

    def __init__(self, name_type, size, price_per_kilo):
        self.name_type = name_type
        self.size = size
        self.price_per_kilo = price_per_kilo

    def apple_price_multiple_kilo(self, kilo):
        return self.price_per_kilo * kilo
