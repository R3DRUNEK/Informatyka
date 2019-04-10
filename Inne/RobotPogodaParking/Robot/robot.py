def dyskwalifikacja(stri):
    x = 0
    y = 0
    for i in range(len(stri)):
        if stri[i] == 'N':
            y -= 1
        elif stri[i] == 'E':
            x += 1
        elif stri[i] == 'S':
            y += 1
        elif stri[i] == 'W':
            x -= 1
        if x == 20 or x == -1 or y == 20 or y == -1:
            return 1
    return 0


def maxpkt(stri):
    plansza = open("plansza.txt")
    planszatab = list()
    pkt = 0
    x = 0
    y = 0
    for i in plansza:
        planszatab.append(i.strip().replace(" ", ""))
    for i in range(len(stri)):
        if stri[i] == 'N':
            y -= 1
            pkt += int(planszatab[x][y])
        elif stri[i] == 'E':
            x += 1
            pkt += int(planszatab[x][y])
        elif stri[i] == 'S':
            y += 1
            pkt += int(planszatab[x][y])
        elif stri[i] == 'W':
            x -= 1
            pkt += int(planszatab[x][y])
    return pkt


def wielokrotne(stri):
    licz = 0
    naj = 0
    for i in range(len(stri)):
        if stri[i] == "E" or stri[i] == "W":
            licz += 1
        else:
            if licz > naj:
                naj = licz
            licz = 0
    if licz > naj:
        naj = licz
    return naj


robotkr = open("robot.txt")
licznik = 0
lest = 0
maxx = list()
najw = list()
for x in robotkr:
    if dyskwalifikacja(x.strip()) == 1:
        licznik += 1
    else:
        maxx.append(maxpkt(x.strip())+3)
    najw.append(wielokrotne(x))

print(max(maxx), licznik, max(najw))
robotkr.close()
robotkr = open("robot.txt")
for x in robotkr:
    lest += 1
    if wielokrotne(x) == max(najw):
        print(lest)
    if dyskwalifikacja(x.strip()) == 1:
        licznik += 1
    elif maxpkt(x)+3 == max(maxx):
        print(lest)
