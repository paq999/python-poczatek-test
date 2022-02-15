class Product:
    pass


class Order:
    pass


class Apples:
    pass


class Potatos:
    pass


apple_a, applple_b, potatos_a, potatos_b = Apples(), Apples(), Potatos(), Potatos()

print('type: ', type(apple_a), type(potatos_b))

order_list = [Order() for _ in range(5)]


product_dict = {
    'bread': Product(),
    'pasta': Product(),
    'milk drink': Product(),
    'meal': Product(),
    'rise': Product()
}

print(order_list, product_dict)