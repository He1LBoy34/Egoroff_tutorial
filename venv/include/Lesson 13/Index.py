a = [43, 23, 54, 25, 27]

print(a[0])
print(a[1:3])

print(a[:3])
print(a[2:])

print(a[:])

print(a[::2])  # третий параметр это шаг, первые два от и до каого

a[0] = 0

print(a[0])

del a[0]
print(a)