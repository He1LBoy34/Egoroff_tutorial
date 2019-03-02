guess = input('Insert password: \n')
password = 'qwerty'
while guess != password:
    print("incorrect input")
    guess = input('Insert password: \n')
print('sucsesful input')