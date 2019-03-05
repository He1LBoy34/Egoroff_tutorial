s = 'Hello world'
for i in s:
    if 'a' <= i <= 'z':
        print(i, 'Small')
    elif 'A' <= i <= 'Z':
        print(i, 'Big')
    else:
        print(i)