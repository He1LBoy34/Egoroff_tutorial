while True:
    a = input()
    if a == "Exit":
        break
    if len(a) < 5:
        continue
    print(a, len(a))