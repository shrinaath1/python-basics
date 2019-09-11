import random
import turtle
screen = turtle.Screen()
screen.setup(600,400,-300,-200)
bnd = turtle.Turtle()
char = turtle.Turtle()
chars = []
for c in range(0, 6):
    chars.append(turtle.Turtle())
score=0
speed=0
def setup():
  screen.bgcolor("green")
  bnd.pensize(3)
  bnd.pencolor("red")
  bnd.penup()
  bnd.setposition(-300, -200)
  bnd.pendown()
  for side in range(1, 5):
    if (side % 2 == 0):
      bnd.forward(400)
    else:
      bnd.forward(600)
    bnd.left(90)
  bnd.hideturtle()
  char.pencolor("white")
  char.fillcolor("white")
  char.penup()
  for c in range(0, 6):
      chars[c].penup()
      chars[c].setposition(random.randrange(-275, 275), random.randrange(-180, 180))
      chars[c].left(random.randrange(0,90))
      chars[c].shape("circle")
      chars[c].color("red")

def game():
    screen.tracer(3)
    def Acc():
        global speed
        speed+=1
        char.speed(speed)
    def Dec():
        global speed
        speed-=1
        char.speed(speed)
    def Left():
        char.left(45)
    def Right():
        char.right(45)
        char.penup()
    while True:
        char.forward(speed)
        for c in range(0,6):
            chars[c].forward(1)
        screen.listen()
        screen.onkeypress(Acc,"Up")
        screen.onkeypress(Dec,"Down")
        screen.onkeypress(Left,"Left")
        screen.onkeypress(Right,"Right")
        x1 = int(char.xcor())
        y1 = int(char.ycor())
        for c in range(0,6):
            x2 = int(chars[c].xcor())
            y2 = int(chars[c].ycor())
            x=abs(x1-x2)
            y=abs(y1-y2)
            if(x<15 and  y<15):
                chars[c].hideturtle()
                chars[c].setposition(random.randrange(-275, 275), random.randrange(-180, 180))
                chars[c].left(random.randrange(0,90))
                chars[c].showturtle()
                global score
                score+=speed
            xco=abs(chars[c].xcor())
            yco=abs(chars[c].ycor())
            if (xco> 280 or  yco> 180):
                chars[c].left(30)
        x1=abs(char.xcor())
        x2=abs(char.ycor())
        if(x1>300 or x2>200):
            char.hideturtle()
            screen._write((0, 50),"GAME OVER", "center", "Arial", "White")
            screen._write((0,0),f"Your Score:{score}","center","Arial","White")
setup()
game()


