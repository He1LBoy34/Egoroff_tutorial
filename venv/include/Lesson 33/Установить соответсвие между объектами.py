words = {}

while True:
    s = input()
    if s in words:
        print('Слово', s, 'переводится как', words[s])
    else:
        words[s] = input('Введите перевод слова: \n')