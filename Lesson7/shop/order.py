import random
from .product import Product
from .orderelement import OrderElement


class Order:

    def __init__(self, first_name, second_name, order_elements=None):
        self.first_name = first_name
        self.second_name = second_name

        if order_elements is None:
            order_elements = []

        self.order_elements = order_elements
        self.total_price = self.calculate_total_price()

    def print_order(self):
        print(30 * '=')
        print(f'{self.first_name} {self.second_name}')
        print('Zamówił:')
        for element in self.order_elements:
            element.print_order_element()

    def calculate_total_price(self):
        total_price = 0
        for element in self.order_elements:
            total_price += element.price_element()

        return total_price


def generate_order():
    elements_list = []
    rand = random.randint(1, 20)
    for i in range(rand):
        product = Product(f'Product-{i + 1}', 'school', 10 + i)
        quantity = random.randint(1, 10)
        elements_list.append(OrderElement(product, quantity))

    order = Order('Rafał', 'Pająk', elements_list)

    return order
