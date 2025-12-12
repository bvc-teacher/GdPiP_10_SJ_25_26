# https://www.michael-holzapfel.de/themen/sterne/stern5-6.gif
 
import turtle
t = turtle.Turtle()
t.speed(0) 

s = turtle.Screen()
s.setup(width=600, height=800) 
s.setworldcoordinates(-180, -380, 180, 380) 

t.pensize(2)
t.pencolor('black')

t.penup()
t.goto(0, -60) 
t.pendown()

t.fillcolor('yellow')
t.begin_fill()

laenge = 120
t.setheading(0) 
t.right(30)
for _ in range(5):
    t.forward(laenge)
    t.left(36)
    t.forward(laenge)
    t.right(108)

t.end_fill()

t.hideturtle()
s.exitonclick()