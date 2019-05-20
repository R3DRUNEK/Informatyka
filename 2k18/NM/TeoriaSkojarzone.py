def czy_skojarzone(a):
    suma = 0
    for i in range(1, a):
        if a % i == 0:
            suma += i
    suma2 = 0
    for i in range(1, suma-1):
        if (suma-1) % i == 0:
            suma2 += i
    if suma2 == a + 1:
        return "jest skojarzona", suma-1
    else:
        return "nie"

def l_skojarzona(a):
    suma = 1
    i = 2
    while i * i <= a:
        if a % i == 0:
            suma = suma + 1
            if a // i != i:
                suma = suma + a/i
        i = i + 1
    return suma


print(czy_skojarzone(2))
x = l_skojarzona(195)
y = l_skojarzona(x - 1)
if y - 1 == 195:
    print(x - 1)
else:
    print("NIE")