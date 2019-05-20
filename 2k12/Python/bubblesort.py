

def buble(tab):
    for i in range(len(tab)):
        for j in range(len(tab)-i-1):
            if tab[j] > tab[j+1]:
                tab[j], tab[j+1] = tab[j+1], tab[j]
    return tab

x = lambda n : format(n, 'b')

print(int("101", 2))

print(x(11))
print(buble([10, 5, 3, 2, 1]))