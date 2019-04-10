listay = list()
listastr = list()
listazap = list()
check = float('inf')
count = 0
mins = 0
minsbin = ""


def czydwucykliczny(str):
    global listay
    listax = list()
    # if len(str.strip()) == 4:
    #     return 0
    listax.append(str[0:len(str)//2].strip())
    listax.append(str[len(str)//2:len(str)].strip())
    if listax[0] == listax[1]:
        listay.append(str.strip())
        return 1
    else:
        return 0


def zapisy(str):
    global listastr
    global check
    global count
    j = 0
    for i in range(len(str.strip()) // 4):
        if int(str[j:j+4], 2) > 9:
            count += 1
            if len(str.strip()) < check:
                check = len(str.strip())
            return
        j += 4


def zapisb(str):
    global listazap
    global mins
    global minsbin
    if int(str, 2) > 65535:
        return
    else:
        if int(str, 2) > mins:
            mins = int(str, 2)
            minsbin = str


binary = open("binarne.txt")

licznik = 0
for x in binary:
    licznik += czydwucykliczny(x)
    zapisy(x)
    zapisb(x)
get_bin = lambda x: format(x, 'b')

print(licznik)
print(count, check)
print(mins, minsbin)