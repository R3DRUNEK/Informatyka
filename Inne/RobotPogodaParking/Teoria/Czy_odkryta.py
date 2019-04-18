def czy_odkryta(n):
    pom = n
    while n > 0:
        if n % 10 != 0 and pom % (n % 10) != 0:
            return False
        n = n // 10
    return True

print(czy_odkryta(250))

