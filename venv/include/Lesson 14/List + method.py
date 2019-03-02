s = [43, 2, 23, 234, 1, 48, 2, 2, 2]
s.append(23)
print(s)

d = [1, 2, 3, 4]
d.clear()
print(d)

d = s.copy()
print(d)

print(s.count(2))

print(s.index(234))

s.insert(0, 100)
print(s)

s.pop(0)

print(s)

while 2 in s:
    s.remove(2)
    print(s)
s.sort()
s.reverse()
print(s)
