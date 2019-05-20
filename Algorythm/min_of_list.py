import random


def minlist():
    listx = [random.randint(0, 50) for x in range(0, 10)]
    minx = listx[0]
    print(listx)
    for x in listx:
        if x <= minx:
            minx = x
    print(minx)


minlist()
