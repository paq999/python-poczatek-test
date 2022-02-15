from shop.order import generate_order
from shop.apple import Apple
from shop.potato import Potato

if __name__ == '__main__':
    order_1 = generate_order()
    order_1.print_order()

    apple_1 = Apple('red', '7', 30)
    price = apple_1.apple_price_multiple_kilo(10)
    print(f"Cena jabłek wynosi: {price} zł.")




