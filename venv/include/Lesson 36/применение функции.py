a = int(input('Введите сторону куба в пикселях: '))
import turtle

turtle.speed(1)

c = a / 2


def parallel_move():
    turtle.forward(c)
    turtle.backward(c)


def move(a):
    turtle.forward(a)
    turtle.left(90)


def draw_square(a):
    for i in range(4):
        move(a)


if a > 50:
    turtle.penup()
    turtle.setx(a - a * 1.5)
    turtle.sety(a - a * 1.5)
    turtle.pendown()

turtle.forward(a)
turtle.left(30)

parallel_move()

turtle.left(60)
turtle.forward(a)
turtle.right(60)

parallel_move()

turtle.left(150)
turtle.forward(a)
turtle.right(150)

parallel_move()

turtle.left(240)
turtle.forward(a)
turtle.right(240)

turtle.forward(c)
turtle.right(30)

draw_square(a)
