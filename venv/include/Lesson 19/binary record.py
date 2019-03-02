x = int(input('Введите число для перевода в двоичную запись: \n'))

while x > 0:
    last = x % 2
    print(last)
    x = x // 2
