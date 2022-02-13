import excurse1

time = input('Podaj czas biegu: ')
distanse = input('Podaj długgość biegu: ')

speed = excurse1.run_speed(distanse, time)
print(f"Szybkość biegu to {speed}")