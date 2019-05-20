counter = 0
two = 0
eight = 0

def z1(string):
    zero = 0
    one = 0
    global counter
    for i in string:
        if i == "0":
            zero += 1
        else:
            one += 1
    if zero > one:
        counter += 1


def z2(string):
    global two
    global eight
    if int(string, 2) % 2 == 0:
        two += 1
    if int(string, 2) % 8 == 0:
        eight += 1



file = open("liczby.txt")
listax = []
for x in file:
    z1(x.strip())
    z2(x.strip())
    listax.append(int(x.strip(), 2))


print(counter)
print(two, eight)

for i in range(len(listax)):
    if listax[i] == max(listax):
        print("max", i)
    if listax[i] == min(listax):
        print("min", i)
