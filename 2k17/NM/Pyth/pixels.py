maxp = 0
minp = 256
listax = []
ilew = 0
iles = 0
maxl = 1

def z1(string):
    global maxp
    global minp
    if max(string) > maxp:
        maxp = max(string)
    if min(string) < minp:
        minp = min(string)

def z2(string):
    global ilew
    for i in range(len(string)//2):
        if string[i] != string[len(string)-(1+i)]:
            ilew += 1
            return
def z3():
    global iles
    global listax
    for i in range(len(listax)):
        for y in range(len(listax[i])):
                if y < len(listax[i])-1 and abs(listax[i][y]-listax[i][y+1]) > 128:
                    iles += 1
                    continue
                if y > 0 and abs(listax[i][y]-listax[i][y-1]) > 128:
                    iles += 1
                    continue
                if i > 0 and abs(listax[i][y]-listax[i-1][y]) > 128:
                    iles += 1
                    continue
                if i < len(listax)-1 and abs(listax[i][y]-listax[i+1][y]) > 128:
                    iles += 1
                    continue

def z4():
    global maxl
    global listax
    licz = 1
    for x in range(len(listax[0])):
        for y in range(len(listax)-1):
            if listax[y][x] == listax[y+1][x]:
                licz += 1
            else:
                if licz > maxl:
                    maxl = licz
                licz = 1



file = open("dane.txt")
for string in file:
    listax.append(string.strip().split())

for x in range(len(listax)):
    for y in range(len(listax[x])):
        listax[x][y] = int(listax[x][y])

for x in listax:
    z1(x)
    z2(x)

z3()
z4()
print(maxp, minp, ilew, iles, maxl)