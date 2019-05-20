import math
from functools import reduce


items = [1, 2, 3, 4, 5]

squared = list(map(lambda x: x**2, items))

print(squared)


def multiply(x):
    return x*x


def add(x):
    return x+x


funcs = [multiply, add]

for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)


number_list = range(-5, 5)

less_then_zero = list(filter(lambda x: x < 0, number_list))

print(less_then_zero)

product = reduce(lambda x, y: x*y, [1, 2, 3, 4])

print(product)


print(math.gcd(60, 10))



test = [1, 1, 2, 4, 5, 6, 7, 7, 10, 20, 20, 20, 3]

print(max(set(test), key=test.count))

print(test.index(max(test)))

test = [1, 1, 2, 3, 4]

print(list(set(test)))


d = {'orange': 10, 'apple': 20}

print(sorted(d, key=lambda x: x[1]))
