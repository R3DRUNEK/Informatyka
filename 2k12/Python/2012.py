wyjscie = open("wyjscie.txt", "w")
def z1(word, key):
    new_word = ""
    j = 0
    for i in range(len(word)):
        if (ord(word[i])+ord(key[j])-64) > 90:
            new_word += chr((ord(word[i])+ord(key[j])-64) - 26)
        else:
            new_word += chr(ord(word[i])+ord(key[j])-64)
        j += 1
        if j >= len(key):
            j = 0

def z2(word, key):
    new_word = ""
    j = 0
    global wyjscie
    for i in range(len(word)):
        if (ord(word[i])-(ord(key[j])-64)) < 65:
            new_word += chr((ord(word[i])-(ord(key[j])-64)) + 26)
        else:
            new_word += chr(ord(word[i])-(ord(key[j])-64))
        j += 1
        if j >= len(key):
            j = 0
    wyjscie.write(new_word + "\n")
    print(new_word)


notdecrypted = open("tj.txt")
keys = open("klucze1.txt")
decrypted = open("sz.txt")
keys2 = open("klucze2.txt")


for x, y in zip(notdecrypted, keys):
    z1(x.strip(), y.strip())

decrypted = [1, 2, 4, "d", 54]
keys2 = [5, 3, 2, 1]
for i, (x, y) in enumerate(zip(decrypted, keys2)):
    print(x, i)
    print(y)
