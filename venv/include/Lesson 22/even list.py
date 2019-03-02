a = [54, 22, 36, 40]
# YES - all even
# No - else
while len(a) > 0:
    last = a.pop()
    if last % 2 != 0:
        print("No")
        break
else:
    print("Yes")
