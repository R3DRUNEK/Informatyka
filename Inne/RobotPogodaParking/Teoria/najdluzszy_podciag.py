def najdluzszy_podciag(n, tab):
    j = 0
    licz = 1
    for i in range(n):
        if tab[i] == licz:
            j += 1
            licz += 1
    return j


tab = [0, 2, 3, 1, 5, 2, 3, 10, 15, 32, 13, 12, 13, 20, 14, 15, 4]




print(najdluzszy_podciag(len(tab), tab))