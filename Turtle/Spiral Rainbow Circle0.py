import turtle
drawing_area = turtle.Screen()
drawing_area.setup(width=650,height=650)
turtle.bgcolor("black")
turtle.pensize(2)
turtle.speed(0)
for i in range(10):
    for colors in ["red","blue","yellow","orange","purple","teal"]:
        turtle.color(colors)
        turtle.circle(100)
        turtle.left(10)
turtle.hideturtle()