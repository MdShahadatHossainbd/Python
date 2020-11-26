import turtle
drawing_area = turtle.Screen()
drawing_area.setup(width=650,height=650)

turtle.speed(0)
turtle.bgcolor("black")

for i in range(10):
    for colors in ["blue", "red", "orange", "purple"]:
        turtle.color(colors)
        turtle.pensize(3)
        turtle.left(12)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)
        turtle.forward(200)
        turtle.left(90)