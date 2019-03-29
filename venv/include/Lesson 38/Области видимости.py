def s():
    #local
    a, b, c = 1, 2, 3
    w = 'HELLO WORLD'
    print(id(w), 'local id')
    print(a, b, c, w)

def q():
    r, t = 5, 7
    print(r, t)

s()
q()

#global
w = 'Hello World!'
d = 100

print(w)
print(id(w), 'global id')

def v():
    global sa
    sa = 10

sa = 20

v()

print(sa)