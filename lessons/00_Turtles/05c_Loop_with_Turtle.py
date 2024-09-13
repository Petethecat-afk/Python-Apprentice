
"""
Turtles with a loop. 

Study the previous program, 05a_Loop_with_Turtle.py, and then
write a new program that uses a loop to draw a pentagon.
( You can cut and past most of it! )


import turtle                           # Tell Python we want to work with the turtle
turtle.setup (width=600, height=600)    # Set the size of the window
"""
import turtle                           # Tell Python we want to work with the turtle
turtle.setup(width=600, height=600)     # Set the size of the window

tina = turtle.Turtle()  

tina.speed(1)

tina.begin_fill()
tina.circle(130)
tina.fillcolor("red")
tina.end_fill()


tina.penup()
tina.left(90)
tina.forward(30)
tina.pendown()


tina.begin_fill()
tina.right(90)
tina.circle(100)
tina.fillcolor("white")
tina.end_fill()

tina.penup()
tina.left(90)
tina.forward(30)
tina.pendown()

tina.begin_fill()
tina.right(90)
tina.circle(70)
tina.fillcolor("red")
tina.end_fill()

tina.penup()
tina.left(90)
tina.forward(30)
tina.pendown()

tina.begin_fill()
tina.right(90)
tina.circle(40)
tina.fillcolor("blue")
tina.end_fill()

tina.penup()
tina.left(150)
tina.forward(40)
tina.pendown()



turtle.exitonclick()   