import random


class Product:

    def __init__(self, name, name_category, unit_price):
        self.name = name
        self.name_category = name_category
        self.unit_price = unit_price


class Order:

    def __init__(self, first_name, second_name, products=None):
        self.first_name = first_name
        self.second_name = second_name

        if products is None:
            self.products = []
        else:
            self.products = products

        self.price = sum(x.unit_price for x in self.products)


class Apple:

    def __init__(self, name_type, size, price_per_kilo):
        self.name_type = name_type
        self.size = size
        self.price_per_kilo = price_per_kilo


class Potato:

    def __init__(self, name_type, size, price_per_kilo):
        self.name_type = name_type
        self.size = size
        self.price_per_kilo = price_per_kilo


product_1 = Product('ball', 'sport', 120)
product_2 = Product('bed', 'home', 1200)
order_1 = Order('Rafał', 'Pająk')
order_2 = Order('Rafał', 'Pająk', [product_1, product_2])
apple_1 = Apple('red', 10, 1.5)
apple_2 = Apple('yellow', 12, 2)
potato_1 = Potato('poland', 7, 0.5)
potato_2 = Potato('italy', 8, 0.8)


def print_order(order):

    print(f'{order.first_name} {order.second_name} - zamówił: {[x.name for x in order.products]} - za: {order.price}')


def generate_product():

    product_list = []
    rand = random.randint(1, 20)
    for i in range(rand):
        product_list.append(Product(f'Product-{i+1}', 'school', 10 + i))

    return product_list


print_order(order_2)
for product in generate_product():
    print(f'{product.name} - {product.name_category} -{product.unit_price}')

