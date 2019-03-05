vowels = 'aeiou'
s = 'aertiooikjoaikl'
for i in range(len(s) - 1):
    if s[i] in vowels and s[i + 1] in vowels:
        print(s[i], s[i + 1])