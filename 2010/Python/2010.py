wyjscie = open("odp_4a.txt", "w")
wyjscie2 = open("odp_4b.txt", "w")
def z1(x):
    ilosc = len(x[0])
    for i in x:
        if len(i) != ilosc:
            return
    global wyjscie
    wyjscie.write(str(x)+"\n")

def z2(x):
    stringx = list(x[0])
    for i in x:
        if sorted(stringx) != sorted(i):
            return
    global wyjscie2
    wyjscie2.write(str(x)+"\n")









file = open("anagram.txt")

for x in file:
    z1(x.strip().split())
    z2(x.strip().split())



