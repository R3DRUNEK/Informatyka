def oprocentowanie(x, n, r):
    odsetki = 0
    for y in range(n):
        odsetki += (x+odsetki) * (r/100)
    return odsetki + x


print(oprocentowanie(500, 2, 1))
procent = 1
x = 500
for y in range(2):
    print(x + x*procent/100)

# a = int(input("Podaj liczbe"))
# b = int(input("Podaj liczbe"))
# c = int(input("Podaj liczbe"))
# d = int(input("Podaj liczbe"))
# e = int(input("Podaj liczbe"))
# srednia = (a + b + c + d + e ) / 5

samogloski = ['a', 'o', 'e', 'i', 'u', 'y', 'ó']
tekst = "hej, asd"
liczniksamo = 0
licznikspol = 0
for x in tekst:
        if x in samogloski:
            liczniksamo += 1

for x in tekst:
    if x not in samogloski:
        licznikspol += 1

txt = ",,,,,ssaaww.....banana...."
interpunction = ['!', ' ', ',', '.']
new_txt = ""
for x in txt:
    if x not in interpunction:
        new_txt += x

txt = "hajkowe"
n_txt = ""
for x in txt:
    if x == 'a':
        n_txt += 'e'
    elif x == 'e':
        n_txt += 'o'
    elif x == 'o':
        n_txt += 'a'
    else:
        n_txt += x
print(n_txt)

txt = txt.replace("a", "E")
txt = txt.replace("e", "O")
txt = txt.replace("o", "A")
txt = txt.lower()
print(txt)
txt2 = "dobrze"
ind = txt2.index('o')
print(txt2[0:ind+1])
