v = iter(range(5))

print(next(v))
print(next(v))
print(next(v))

print(v.__next__())  # альтернативная запись итерируемого объекта
# итерируемый объект можно передавать пока есть значения в range, после выпадает ошибка
# при обходе числа создаётся итератор, который запоминает на каком мы сейчас числе

n = iter([43, True, "Hello"])   # к итерируемы объектам так же можно отнести списки
print(n.__next__())
print(n.__next__())
print(n.__next__())

m = iter('Hello')
print(m.__next__())
print(m.__next__())
print(m.__next__())

# числа не являются итерируемыми объектами

for i in range(5):
    print(i)
