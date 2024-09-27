
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
tina.left(155)
tina.forward(28)
tina.pendown()

tina.penup()
tina.begin_fill()
tina.right(85)
tina.forward(75)
tina.fillcolor("white")
tina.right(141)
tina.forward(80)

tina.right(148)
tina.forward(80)

tina.right(141)
tina.forward(75)

tina.right(144)
tina.forward(81)
tina.end_fill()
tina.pendown()

tina.penup()



tina.right(180)
tina.forward(32)
tina.begin_fill()
tina.fillcolor("white")
tina.left(112)
tina.forward(20)

tina.right(80)
tina.forward(20)

tina.right(70)
tina.forward(23)


tina.right(80)
tina.forward(23)

tina.right(74)
tina.forward(20)

tina.end_fill()

tina.forward(100)



turtle.exitonclick()   