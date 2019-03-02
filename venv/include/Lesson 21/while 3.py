n = int(input("insert number: \n"))
i = 1
while i <= n ** 0.5:
    if n % i == 0:
        print(i, n // i)