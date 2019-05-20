def silnia(params):
    u""""" Silnia @liczba
    Zwraca silnię danej liczby
    """
    if params == 0:
        return 1
    return params*silnia(params-1)


print(silnia(3))
