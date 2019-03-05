a = [2, 2, 2, 23, 23, 24, 24]
b = []

for i in a:
    if not i in b:
        b.append(i)
print(b)