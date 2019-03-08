# Цикл называется вложенным если он расолагается внутри другого цикла

for i in range(1, 10):
    for j in range(1, i + 1):
        print(j, end='')
    print()
