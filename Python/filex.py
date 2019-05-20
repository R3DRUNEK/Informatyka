def plik(x, y):
    dane = open(x)
    tablica = []
    array = []
    i = 0
    k = 0
    c = 0
    for linia in dane:
        # tablica.append(str(int(linia.strip(), y)))
        tablica.append(linia.strip())
    for x in tablica:
        maks = x[0]
        if x[0] == x[len(x)-1]:
            i += 1
        for y in range(1, len(x)):
            if x[y] >= maks:
                maks = x[y]
                k += 1
            if k == len(x)-1:
                array.append(int(x))
                c += 1
        k = 0
    dane.close()
    return array


def minmax(x):
    maksx = 0
    minx = x[0]
    for y in range(0, len(x)):
        if x[y] > maksx:
            maksx = x[y]
        if x[y] < minx:
            minx = x[y]
    return maksx, minx


print(plik('dane.txt', 8))
print(minmax(plik('dane.txt', 8)))
