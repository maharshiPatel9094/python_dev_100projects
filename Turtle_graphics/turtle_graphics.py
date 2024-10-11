# from turtle import Turtle,Screen


# tinny_the_turtle = Turtle()
# change the shape
# tinny_the_turtle.shape("turtle")
# change the color
# when want to use colorstring or rgb use pencolor() it takes color from TK which is tkinter built in commands 
# Turtle uses tkinter for underlying graphics
# tinny_the_turtle.color("red")
# tinny_the_turtle.pencolor('#32c18f')
# tinny_the_turtle.pencolor('red')


# get the screen 
# screen = Screen()
# exit the screen on click
# screen.exitonclick()

# move forward
# tinny_the_turtle.forward(100) #takes distance as input
# tinny_the_turtle.right(90) #takes angle as input

# challenge-1 -> draw the square 100*100

# method -1
# tinny_the_turtle.forward(100)
# tinny_the_turtle.right(90)
# tinny_the_turtle.forward(100)
# tinny_the_turtle.right(90)
# tinny_the_turtle.forward(100)
# tinny_the_turtle.right(90)
# tinny_the_turtle.forward(100)
# tinny_the_turtle.right(90)

# method-2
# for i in range(4):
#     tinny_the_turtle.forward(100)
#     tinny_the_turtle.right(90)


#------------------------------------------- importing the modules teachniques---------------------------------------
# import turtle
# tim = turtle.Turtle()

# from turtle import Turtle
# tim = Turtle()

# from turtle import * -> confusing when we write code somewhere in the middle of the project

# -------------------Aliasing modules------------------------------------------
# import turtle as t
# tim = t.Turtle()

# -------------------Installing modules-------------------------------------------
# there are some modules which can not be imported
# we can install them using pip install module_name from python packages
# pip install turtle
# pip install pygame
# pip install matplotlib
# pip install pandas
# import heroes
# print(heroes.gen()

# --------------------Virtual env---------------
# virtualenv is a tool to create isolated python environment
# it is used to install packages without affecting the system python packages
# we can install virtualenv using pip install virtualenv
# we can create virtualenv using virtualenv venv
# we can activate virtualenv using source venv/bin/activate
# we can deactivate virtualenv using deactivate

# A Python virtual environment is an isolated environment that allows you to manage dependencies for different projects separately. By using virtual environments, you can avoid conflicts between project dependencies, especially when different projects require different versions of the same library.

# ------------------------challenge-2----------------------------------
# draw a dashed line 
# we can also give the width by pensize() set the width
# from turtle import Turtle,Screen
# tim = Turtle()
# for i in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
# # screen setup
# screen = Screen()
# screen.exitonclick()


# ----------------challenge-3----------------------
# draw a triangle,square,pentagon,hexagon,heptagon.ocatgon.nonagon and decagon
# side = 100
# from turtle import Turtle,Screen
# tim = Turtle()
# # triangle - side = 360/3 =120
# def draw_shape(num_sides):
#         angle = 360 / num_sides
#         for _ in range(num_sides):
#             tim.forward(100)
#             tim.right(angle)
            
# for  shape_side in range(3,11):
#     draw_shape(shape_side)   
        
# # screen setup 
# screen = Screen()
# screen.exitonclick()

# from turtle import Turtle,Screen
# import random
# turtle setup
# tim = Turtle()

#define the walk distance
# move_distance = 30

# set the angles
# setheading() -> takes the angle and change the turtle direction in one of the given angles
# angles = [0,90,180,270]


# random walk
# for _ in range(300):
    # tim.setheading(random.choice(angles))
    # r = random.randint(0,255)
    # g = random.randint(0,255)
    # b = random.randint(0,255)
    # width and pensize do the same thing
    # tim.width(15)
    # tim.color(random.random(),random.random(),random.random())
    # tim.speed("fastest")
    # tim.forward(move_distance)

# screen setup 
# screen = Screen()
# screen.exitonclick()



# ---------------------------------challenge-5-------------------------------
# make a spirograph
from turtle import Turtle,Screen
import random
# set object
tim = Turtle()

angles = [0,90,180,270]

# for _ in range(200):
#     tim.setheading(random.randint(0,360))
#     tim.color(random.random(),random.random(),random.random())
#     tim.speed("fastest")
#     tim.circle(100)

tim.speed("fastest")
def draw_spirograph(size_gap):
    for _ in range(int(360 / size_gap)):
        tim.color(random.random(),random.random(),random.random())
        tim.circle(100)
        # setheading change turtle in specific direction
        # Returns the current heading (direction) of the turtle in degrees.
        tim.setheading(tim.heading() + size_gap)

        
draw_spirograph(5)



# set screen
screen=Screen()
screen.exitonclick()