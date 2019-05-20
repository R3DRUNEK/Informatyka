import random


def generate():
    charslist = [chr(x) for x in range(97, 123)]
    charslist.append(' ')
    guess = ""
    for i in range(28):
        i = random.choice(charslist)
        guess += i
    return guess


def compare(guess):
    score = 0
    search = "methinks it is like a weasel"
    for i, (x, y) in enumerate(zip(guess, search)):
            if x == y:
                score += 1
    return score


def genscore():
    dictx = {}
    for i in range(1000):
        x = generate()
        y = compare(x)
        dictx[y] = x
        # if y == 27:
        #     print(x)
        #     break
    return dictx


def main():
    high = 0
    x = 0
    while high < 10:
        x = genscore()
        high = max(x)
    print(x[high])


if __name__ == "__main__":
    main()
