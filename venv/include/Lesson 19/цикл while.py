x = int(input('введите число для обхода: \n'))
kol = 0
kol_ch = 0
kol_ne_ch = 0
s = 0
pr = 1
maxim = 0
minim = 9
while x > 0:
    last = x % 10
    kol += 1
    if last % 2 == 0:
        kol_ch += 1
    if last % 2 == 1:
        kol_ne_ch += 1
    s += last
    pr *= last
    if last > maxim:
        maxim = last
    if last < minim:
        minim = last
    x = x // 10
print('Всего цифр:', kol)
print('Всего чётных цифр:', kol_ch)
print('Всего не чётных цифр:', kol_ne_ch)
print('Сумма цифр:', s)
print('Произведение:', pr)
print('Максимальное число:', maxim)
print('Минимальное число:', minim)
