alfabet = [chr(x) for x in range(ord('A'), ord('Z')+1)]
listax = []
listay = []
listaz = []


def z1(string):
    new_word = ""
    k = 107
    for x in string:
        new_word += alfabet[(ord(x)-ord('A') + k) % len(alfabet)]
    listax.append(new_word)

def z2(string):
    decrypted = string[0]
    if len(string) == 1:
        listay.append(string)
        return
    else:
        k = int(string[1])
        new_word = ""
        for x in decrypted:
            miejsce = ord(x) - ord('A')
            if miejsce - k % 26 >= 0:
                new_word += alfabet[miejsce - k % 26]
            else:
                new_word += alfabet[(miejsce - (k % 26))+26]
        listay.append(new_word)


def z3(string):
    n1 = ord(string[1][0])
    n2 = ord(string[0][0])
    if n1 - n2 < 0:
        k = n1 + 26 - n2
    else:
        k = n1 - n2
    print(k)
    for x in range(len(string[0])):
        n3 = ord(string[1][x])
        n4 = ord(string[0][x])
        if n3 - n4 < 0:
            if n3 + 26 - n4 != k:
                listaz.append(string[0])
                break
        elif n3 - n4 != k:
            listaz.append(string[0])
            break


file = open("dane_6_1.txt")
for x in file:
    z1(x.strip())

file2 = open("dane_6_2.txt")
for x in file2:
    z2(x.strip().split())


file3 = open("dane_6_3.txt")
listaz = []
for x in file3:
    z3(x.strip().split())

print(listax)
print(listay)
print(listaz)