import calculations.locate as locate

start = float(input('Podaj startowy kapitał: '))
percent = float(input('Podaj oprocentowanie: '))
duration = float(input("Podaj czas trwania lokaty: "))

value = locate.calc(start, percent, duration)
print(f"Wartość oprocentowania lokaty wynosi {value}")



