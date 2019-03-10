person = {}

s = 'IVANOV IVAN Samara SGU 4 5 4 5 5 5 4'
s = s.split()
person['Last name'] = s[0]
person['First name'] = s[1]
person['City'] = s[2]
person['University'] = s[3]
person['Marks'] = []

for i in s[4:]:
    person['Marks'].append(int(i))

print(person)