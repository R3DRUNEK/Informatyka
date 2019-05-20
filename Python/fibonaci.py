def fib(params):
    u"""" Rekurencyjnie zwraca wyraz n ciągu fibonacciego
    Rekurencja -
    fib(5) -> fib(4) + fib(3)
    fib(4) -> fib(3) + fib(2)
    fib(3) -> fib(2) + fib(1)
    Jeśli z x warunków wynika następny rekurencja works!
    """
    if params == 0:
        return 0
    if params == 1:
        return 1
    return fib(params-1)+fib(params-2)


def fib2(params):
    a, b = 0, 1
    for i in range(params):
        a, b = b, a + b
    return a


print(fib2(15))

