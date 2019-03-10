a = {
    'Moskva': 495,
    'Piter': 812,
    'Penza': 8412
}
d = {
    'Moskva': 495,
    'Piter': 812,
    'Penza': 8412
}
print(d)
print(len(d))
print(1 in d)

for i in d:
    print(i, d[i])

a.clear()
print(a)

print(d.get('Piter'))
print(d.get(1, 'No such key'))
print(d.setdefault(6, 'six'))  # получает значение ключа и создаёт новую пару в случае отсутствия такового
print(d.setdefault('Moskva'))
print(d)
print(d.pop(6))  # возвращает и удаляет значение элемента
print(d.popitem())  # удаляет случайное значение
print(d)
print(d.keys())
for i in d.keys():
    print(i, d[i])
print(d.values())
print(d.items())
for i in d.items():
    print(i)

for key, value in d.items():
    print(key, value)