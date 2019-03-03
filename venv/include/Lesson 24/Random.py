from random import randint
s = 0
for i in range(5):
    a = randint(134, 2333300)
    s += a
    print(a, end=' ')
print()
print(s)
