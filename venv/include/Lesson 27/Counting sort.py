a = [0, 0, 0, 1, 2, 2, 2, 3, 3, 4, 4, 5]

count = [0] * 6

for i in a:
    count[i] += 1
print(count)

for i in range(6):
    if count[i] > 0:
        print((str(i) + ' ') * count[i], end='')
