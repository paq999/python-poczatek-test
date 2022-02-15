class Product:

    def __init__(self, name, name_category, unit_price):
        self.name = name
        self.name_category = name_category
        self.unit_price = unit_price

    def print_self(self):
        print(f'Nazwa: {self.name} - Kategoria: {self.name_category} - Cena: {self.unit_price}')






