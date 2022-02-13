from fruit_store.order import add_shopping_list


def buy_fruits():
    fruit_name = input('Podaj nazwę owocu: ')
    quantity = int(input('Podaj liczbę owoców: '))

    add_shopping_list(fruit_name, quantity)


def run():
    print('witaj w sklepie z owocami!')
    option = None
    while option != 'X':
        buy_fruits()
        option = input("Czy chcesz kantunuować zakupy? Jeżeli nie wciśnij 'X': ").upper()

    print("Twoja lista zakupowa:")
    cumulate_cost = 0
    for item in order.shopping_list:
        for key, val in item.items():
            print(f"owoc: {key}, ilość: {val['quantity']}, cena: {val['cost']}")
            cumulate_cost += val['cost']
    print("=" * 30)
    print(f"Łączny koszt zakupów wynosi: {cumulate_cost} zł.")


if __name__ == "__main__":
    run()
