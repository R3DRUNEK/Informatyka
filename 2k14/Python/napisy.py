licznik = 0
def czy_liczba_pierwsza(x):
    for i in range(2, x//2+1):
        if x % i == 0:
            return 0
    return 1


def z1(x):
    global licznik
    suma = 0
    for i in x:
        suma += ord(i)
    if czy_liczba_pierwsza(suma):
        licznik += 1

def z2(x):
    for i in range(len(x)-1):
        if ord(x[i]) >= ord(x[i+1]):
            return
    # print(x)




file = open("NAPIS.txt")
tab = []

for x in file:
    z1(x.strip())
    z2(x.strip())
    tab.append(x.strip())

for i in range(len(tab)):
    for j in range(i+1, len(tab)):
        if tab[i] == tab[j]:
            print(tab[i])
