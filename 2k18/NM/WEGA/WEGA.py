zad1 = ""
j = 0
minx = 0
var = ""


def napis(stri):
    global j
    global zad1
    j += 1
    if j % 40 == 0:
        zad1 += stri[9]


def rozne(stri):
    global minx, var
    count = 0
    listch = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    for x in range(len(stri)):
        if stri[x] in listch:
            count += 1
            listch.remove(stri[x])
    if count > minx:
        minx = count
        var = stri


def distance(stri):
    check = 0
    dist = [x for x in range(0, ord('Z')+1-ord('A'))]
    for x in range(len(stri)):
        for y in range(len(stri)):
            if abs(dist[ord(stri[x]) - 65] - (dist[ord(stri[y]) - 65])) > 10:
                check = 1
    if check == 0:
        print(stri)


plik = open("sygnaly.txt")

for x in plik:
    napis(x)
    rozne(x)
    distance(x.strip())


print(minx, var)
print(zad1)