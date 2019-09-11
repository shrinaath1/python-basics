import turtle
comb=turtle.Turtle()
screen=turtle.Screen()
comb.pensize(1)
screen.bgcolor("black")
comb.pencolor("red")
comb.speed(10)
side=6
for combs in range(3):
    for sides in range(6):
        for edges in range(1):
            for shs in range(6):
                comb.left(-60)
                comb.forward(side)
            comb.forward(side)
        comb.left(60)
    side=3*side
    comb.penup()
    comb.forward(side)
    comb.left(60)
    comb.forward(side/3)
    comb.pendown()
    comb.left(60)
    for n in range(6):
        comb.forward(side)
        comb.left(60)
screen.exitonclick()
