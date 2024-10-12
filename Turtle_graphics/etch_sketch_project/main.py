# game rules
# w -> forward
# s -> backward
# a -> counter-clockwise
# d -> clockwise
# c -> clear drawing
# h -> home

from turtle import Turtle, Screen

tim = Turtle()

# function to move forward
def move_forward():
    tim.forward(10)

# function to move backward
def move_backward():
    tim.backward(10)
    
# function to move counter-clockwise
def move_counter_clockwise():
    tim.left(10) 
    
# function to move clockwise
def move_clockwise():
    tim.right(10)
    
# function to clear the screen
def clear_screen():
    tim.clear()
    
# function to bring the turtle back home
def bring_home():
    tim.penup()
    tim.home()
    tim.pendown()

# function to increase the turtle speed
def increase_speed():
    tim.speed(10)
    
# function to decrease the turtle speed 
def decrease_speed():
    tim.speed(10)


screen = Screen()
screen.listen()

# Correct key mappings
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_counter_clockwise, "a")
screen.onkey(move_clockwise, "d")
screen.onkey(clear_screen, "c")
screen.onkey(bring_home,"h")
screen.onkey(increase_speed,"Up")
screen.onkey(decrease_speed,"Down")

screen.exitonclick()

