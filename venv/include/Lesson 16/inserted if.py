a = 35
if a % 5 == 0:
    if 9 < a < 100:
        print(1)
        print(2)
    else:
        print(3)
        print(4)

a = int(input())
b = int(input())
c = int(input())

if a < b:
    if a < c:
        print(a)
    else:
        print(c)
else:
    if b < c:
        print(b)
    else:
        print(c)
