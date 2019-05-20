def cube(liczba, potega):
    if potega == 0:
        return 1
    if potega == 1:
        return liczba
    return liczba*cube(liczba, potega-1)


print(cube(2, 10))

