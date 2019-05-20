def czydwucykliczny(str):
    listax = list()
    j = 0
    k = 4
    for i in range(len(str)//4):
        listax.append(str[j:k])
        j += 4
        k += 4
    licznik = 0
    licznik2 = 0
    if len(str) // 4 % 2 != 0:
        return 0
    print(listax)
    for i in range(0, len(listax)):
        for j in range(0, len(listax)):
            if i == j:
                continue
            if listax[i] == listax[j]:
                licznik += 1
                # print(listax[j], "dla ", listax[i], "licznik= ", licznik, "ktore i ", i, "ktore j ", j)
        print(licznik)
        if licznik == 1:
            licznik2 += 1
            licznik = 0
        else:
            return 0
    print("LICZNIK2 = ", licznik2)
    if licznik2 > 1:
        print("PRZESZLO")
        return 1
    else:
        return 0


binary = open("binarne.txt")

licznik = 0
for x in binary:
    licznik += czydwucykliczny(x)

print("licz", licznik)
print("xd", czydwucykliczny("00010001"))