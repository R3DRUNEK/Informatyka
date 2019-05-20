import random


def generate(strlength):
    charslist = [chr(x) for x in range(97, 123)]
    charslist.append(' ')
    guess = ""
    for i in range(strlength):
        i = random.choice(charslist)
        guess += i
    return guess


def compare(guess, goal):
    score = 0
    for i, (x, y) in enumerate(zip(guess, goal)):
            if x == y:
                score += 1
    return score


def main():

    goalstring = "methinks it is like a weasel"
    newscore = 0
    # best = 0
    generateone = ""
    while newscore < 10:
        generateone = generate(28)
        newscore = compare(generateone, goalstring)
        # if newscore >= best:
        #     best = newscore
    print(generateone)


main()
