licznik = 0
licznik2 = 0
listx = []
def z1(x):
    global licznik
    if x[0] == x[len(x)-1]:
        licznik += 1


def z2(x):
    global licznik2
    new_number = int(x, 8)
    if str(new_number)[0] == str(new_number)[len(str(new_number))-1]:
        licznik2 += 1

def z3(x):
    global listx
    for i in range(len(x)-1):
        if int(x[i]) > int(x[i+1]):
                return
    listx.append(int(x))





file = open("dane.txt")

for i in file:
    z1(i.strip())
    z2(i.strip())
    z3(i.strip())


print(licznik, licznik2, min(listx), max(listx), len(listx))