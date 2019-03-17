# Функция - многократно используемые элементы программы
'''
При помощи функции можно объеденить несколько инструкций в один блок
присвоить этому блоку имя
обращаясь к этому блоку по имени выполнить инструкции внутри него в любом месте программы необходимое число раз
'''

def sayHello():
    print('Hello world!')

def square(x):
    print('Квадрат числа', x, '=', x ** 2)

def multiply(a, b):
    print(a * b)

def even(a):
    if a % 2 == 0:
        print(a, 'Even')
    else:
        print(a, 'Not even')

def factorial(n):
    pr = 1
    for i in range(2, n + 1):
        pr = pr * i
    print(pr)

sayHello()
square(25)

for i in range(1, 10):
    square(i)

multiply(3, 5)

even(4)

factorial(23)

if True:
    def primer():
        print('hello')
else:
    def primer():
        print('HELLO')

print(primer())