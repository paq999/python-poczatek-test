def calc(start_capital, interest, duration):
    value = start_capital * pow((1 + interest / 100), duration)
    return value
