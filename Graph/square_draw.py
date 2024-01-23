import turtle

# Створення об'єкта turtle
t = turtle.Turtle()

# Малювання квадрата
for _ in range(4):
    t.forward(10 * 10)  # довжина сторони квадрата - 4 см, переведена у пікселі (1 см = 10 пікселів)
    t.left(90)

# Закриття вікна при кліку
turtle.exitonclick()