"""

Copy the code from the previous lesson, 08a_More_Turtle_programs.ipynb, 
from the section "Change the Turtle Image"


Then change the code so that the turtle has a different image ( look in the 'images'
directory ) and moves to the corners of the screen in a square pattern. 
"""
     
import arrow as arrow

screen = arrow.Screen()
screen.setup(width=600, height=600)
screen.bgcolor('white')

t = arrow.arrom()
t.penup()
t.shape("arrow")


# This is the function that gets called when you click on the screen
def screen_clicked(x, y):

    print('You pressed: x=' + str(x) + ', y=' + str(y))

    t.goto(x, y)
  
screen.onclick(screen_clicked) # Important! Tell Python which function to use when the screen is clicked



t.left(40)
t.forward(100)





arrow.done() # Important! Use 