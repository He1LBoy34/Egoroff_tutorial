print('The perimeter of the triangle')
a = float(input("Please enter first side length: "))
b = float(input("Please enter second side length: "))
c = float(input("Please enter third side length: "))
print("The perimeter of the triangle is equal -", a + b + c)

a, b, c = map(int, input('Такой командой можно вводить значения одной строчкой через пробел: ').split())