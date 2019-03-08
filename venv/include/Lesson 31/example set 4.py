text = input()
a = set()
while text != '':
    words = text.split()
    a.update(words)
    text = input()
print(len(a))