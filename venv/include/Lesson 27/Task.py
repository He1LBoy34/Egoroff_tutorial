s = 'abcxzSADjhbjhBSdHBAS ASDHJB HDABasdhsdh jkjhrtesgf121238768 #@!^#*!^#*%$*&%^*^dadgjbj'

letters = [0] * 26

for i in s.lower():
    if 'a' <= i <= 'z':
        number = ord(i) - 97
        letters[number] += 1

for i in range(26):
    if letters[i] > 0:
        print(chr(i + 97) * letters[i], end='')