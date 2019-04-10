def minkey(listx):
    return float(listx[2])


def najkrotszy():
    global listax
    listanajkr = list(filter(lambda x: float(x[2]) == float(min(listax, key=minkey)[2]), listax))
    return listanajkr


def srodek():
    global listax
    licznik = 0
    max = 0
    ktory = 0
    for i in listax:
        for j in listax:
            if i == j:
                continue
            if pow(float(i[2]), 2) >= pow(float(j[0]) - float(i[0]), 2) + pow(float(j[1]) - float(i[1]), 2):
                licznik += 1
        if licznik > max:
            max = licznik
            ktory = i
        licznik = 0
    return ktory, max


file = open("dane.txt")

listax = []
for x in file:
    listax.append(x.strip().split())

print(najkrotszy())
print(srodek())


