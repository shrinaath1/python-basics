import turtle
import random
scr=turtle.Screen()
b1=turtle.Turtle()
b2=turtle.Turtle()
ball=turtle.Turtle()
scr.setup(600,400,0,0)
scr.bgcolor("green")
scr.title("ping")
b1.penup()
b1.shape("square")
b1.turtlesize(2.5,0.5)
b1.setposition(-280,random.randrange(-180,180))
b1.color("black")
b2.penup()
b2.shape("square")
b2.turtlesize(2.5,0.5)
b2.setposition(280,random.randrange(-180,180))
b2.color("black")
ball.penup()
ball.setposition(0,0)
ball.shape("circle")
ball.speed(1)
scr.tracer(3)
ball.shapesize(0.5,0.5)
ball.color("red")
score1=0
score2=0
y1=0
y2=0
def Up():
    global y1
    y1=b2.ycor()+10
def Down():
    global y1
    y1 = b2.ycor() - 10
def Up1():
    global y2
    y2 = b1.ycor() + 10
def Down1():
    global y2
    y2 = b1.ycor() - 10
while(True):
    scr.listen()
    ball.forward(1)
    scr.onkeypress(Up,"Up")
    b2.goto(b2.xcor(), y1)
    scr.onkeypress(Down,"Down")
    b2.goto(b2.xcor(), y1)
    scr.onkeypress(Up1,"w")
    b1.goto(b1.xcor(), y2)
    scr.onkeypress(Down1,"s")
    b1.goto(b1.xcor(), y2)
    if(abs(ball.ycor())>190):
        ball._rotate(90)
    if(abs(ball.xcor()-b1.xcor())<10):
        ball.left(random.randint(0,30))
    if (abs(ball.xcor() - b2.xcor()) <10):
        ball.right(random.randint(0,30))
    if(abs(ball.xcor())>280):
        scr._delete(ball)
        scr._delete(b1)
        scr._delete(b2)
        scr._write((0,0),"GAME OVER","center","Arial","white")
        break
scr.exitonclick()
