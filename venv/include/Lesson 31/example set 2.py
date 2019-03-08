a = {1, 2, 3, 4}
b = {3, 4, 5, 6, 7}
c = {1, 2, 3, 10, 6, 7}

print(a & b & c)
print(a.intersection(b, c))
print(a | b | c)
print(a.union(b, c))
print(a - b)
print(a ^ b)
print(a == b)
print(a > b)

for i in a:
    print(i)
    