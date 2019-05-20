def z1():
    plik = open("binary.txt")
    tablica = []
    i = 0
    licznik = 0
    for x in plik:
        tablica.append([])
        for y in range(0, len(x), 4):
            tablica[i].append(x[y:y+4].strip())
        i += 1
    for x in tablica:
        x.remove('')
    for x in tablica:
        for y in range(0, len(x)-1):
            print(x[y])


print(z1())
