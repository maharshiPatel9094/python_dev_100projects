# more about turtle graphics
# http://docs.python.org/library/turtle.html
# event listners
# http://docs.python.org/library/turtle.html#event-handling
# state and multiple instances
# higher order functions
from turtle import Turtle,Screen
tim = Turtle()

# function declaration
def move_forward():
    tim.forward(10)


# screen setup 
screen = Screen()
screen.listen()
# when we pass a function to another function we don't pass parenthesis
# whene we pass function without parenthesis it takes the reference of a function 
# when we pass function with parenthesis it calls the function and returns the result
# so here when we press space then only this function will get executed
screen.onkey(fun = move_forward, key="space")
screen.exitonclick()



# ---------Functions as input--------------
# higher order functions
# functions that take other functions as arguments
# functions that return other functions as output
# functions that do both
# functions that take other functions as arguments and return other functions as output
