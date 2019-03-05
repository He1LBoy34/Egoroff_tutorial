a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
even = []
not_even = []
for i in range(len(a)):
    if a[i] % 2 == 0:
        even.append(i + 1)
    else:
        not_even.append(i + 1)
print(even)
print(not_even)