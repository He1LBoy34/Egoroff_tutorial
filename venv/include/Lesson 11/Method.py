s = 'heLLo world'
print(s.upper())
print(s.lower())

# метод не меняет строку

print(s.count('L'))
print(s.find('o'))
print(s.rfind('o'))
print(s.replace('o', '&&&'))
print(s.replace('L', ' ', 3))

print('sdfasdSSDF'.isalpha())
print('231'.isdigit())

d ='111'
print(d.rjust(10, '0'))
print(d.ljust(10, '0'))

w = 'ivanov ivan ivanovich'
print(w.split())
print(w.split('n'))
print(len(w.split()))

k = '5345,345,345,435,345,345,53'
print(k.split(','))
print('='.join(k))

print(','.join(w.split()))

q = '      hello     \n'
print(q)

print(q.strip())
print(q.rstrip())

s = input().upper()
print(s)