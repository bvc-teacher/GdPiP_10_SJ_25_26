# https://www.geogebra.org/classic/chygua4m

import turtle
t = turtle.Turtle()
t.speed(0) 

s = turtle.Screen()
s.setup(width=600, height=800) 
s.setworldcoordinates(-180, -380, 180, 380) 

t.pensize(2)
t.pencolor('black')

# STAMM
t.penup()
t.goto(20, -250) 
t.pendown()
t.fillcolor('brown')
t.begin_fill()

t.goto(20, -350)    
t.goto(-20, -350)   
t.goto(-20, -250)   

t.end_fill()

# BAUM - LINKE SEITE
t.fillcolor('green')
t.begin_fill()

t.goto(-140, -250) 
t.goto(-60, -50)    
t.goto(-120, -50) 
t.goto(-40, 150)    
t.goto(-80, 150)   
t.goto(0, 350)      

# BAUM - RECHTE SEITE
t.goto(80, 150)    
t.goto(40, 150)   
t.goto(120, -50)   
t.goto(60, -50)     
t.goto(140, -250)   
t.goto(20, -250)    

t.end_fill()

t.hideturtle()
s.exitonclick()