class OrderElement:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def print_order_element(self):
        self.product.print_self()

    def price_element(self):
        return self.quantity * self.quantity
