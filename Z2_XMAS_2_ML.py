# https://www.michael-holzapfel.de/themen/sterne/stern5-6.gif
 
import turtle
t = turtle.Turtle()
t.speed(0) 

s = turtle.Screen()
s.setup(width=800, height=600) 
t.pensize(2)
t.pencolor('black')

laenge = 180

t.penup()
t.goto(0, laenge + laenge / 2) 
t.pendown()

t.fillcolor('yellow')
t.begin_fill()

t.setheading(360 - 18) 
t.right(36)
for _ in range(5):
    t.forward(laenge)
    t.left(36)
    t.forward(laenge)
    t.right(108)

t.end_fill()

t.hideturtle()
s.exitonclick()