s = 'Hello world 34 !@#$!@#'
while len(s) > 0:
    if s[0] != ' ':
        print(s[0], end=' ')
    else:
        print(s[0])
    letter = s[0]
    if 'a' <= letter <= 'z':
        print('small')
    elif 'A' <= letter <= 'Z':
        print('big')
    elif letter.isdigit():
        print('digit')
    else:
        print('sing')
    s = s[1:]
