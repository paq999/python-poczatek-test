from .magazin import fruit_shelve

shopping_list = []


def add_shopping_list(fruit_name, quantity):

    if not fruit_name in fruit_shelve.keys():
        print(f'{str(fruit_name).title()} nie ma na półce.')
    else:
        if fruit_shelve[fruit_name]['count'] >= quantity:
            order = {
                fruit_name: {
                    'quantity': quantity,
                    'cost': fruit_shelve[fruit_name]['unit_price'] * quantity
                }
            }

            fruit_shelve[fruit_name]['count'] - quantity
            shopping_list.append(order)
        else:
            print(f'Nie ma wystarczającej ilości {fruit_name}.')




