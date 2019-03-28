def square(x):
    return x ** 2  # return внутри функции работает как break  в цикле

def even(x):
    return x % 2 == 0


a = abs(-7)
b = max(1, 2, 3, 4, 5)

print(a, b)

print(square(4))

for i in range(1, 11):
    print(i, even(i))