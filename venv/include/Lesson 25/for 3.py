a = [32, 33, 5, 22, 76, 6]

# обход по значению

for i in a:
    print(i, a.index(i))

# обход по индексам

for i in range(len(a)):
    print(i, a[i])
    a[i] += 5
print(a)
