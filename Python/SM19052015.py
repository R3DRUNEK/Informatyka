def z1():
    plik = open("slowa.txt")
    licznikzer = 0
    licznikjedynek = 0
    licznik = 0
    for x in plik:
        for y in range(0, len(x)-1):
            if x[y] == '0':
                licznikzer += 1
            else:
                licznikjedynek += 1
        if licznikzer > licznikjedynek:
            licznik += 1
        licznikzer = 0
        licznikjedynek = 0
    plik.close()
    return licznik


def z2():
    plik = open("slowa.txt")
    m = 0
    licznik = 0
    for x in plik:
        if x[0] == '0':
            m = 1
        for y in range(0, len(x)-1):
            if m == 1 and x[y] == '1':
                m = 2
            if m == 2 and x[y] == '0':
                m = 0
        if m == 2:
            licznik += 1
        m = 0
    return licznik


def z3():
    plik = open("slowa.txt")
    m = 0
    k = 0
    tablica = []
    tablicamax = []
    for x in plik:
        for y in range(0, len(x)-1):
            if x[y] == '0':
                k = 1
            if k == 1 and x[y] == '0':
                m += 1
            if m == 10:
                tablicamax.append(x)
            if k == 1 and x[y] == '1':
                k = 0
                tablica.append(m)
                m = 0
            if y == len(x)-2 and x[len(x)-2] == '0':
                tablica.append(m)
        m = 0
        k = 0
    return tablicamax


print(z3())
