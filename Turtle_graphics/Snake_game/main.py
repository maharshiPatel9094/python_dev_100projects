from turtle import Screen
from snake import Snake
import time
# object

# -----------------------step-1 create a snake body
# segment_1 = Turtle("square")
# segment_1.color("white")

# segment_2 = Turtle("square")
# segment_2.color("white")
# segment_2.goto(-20,0)

# segment_3 = Turtle("square")
# segment_3.color("white")
# segment_3.goto(-40,0)
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# turn off the turtle animation 
# when tracer is called we need to update the code so the screen get refresh
screen.tracer(0)

# snake object
snake = Snake()

# snake control
screen.listen()
# when using function as reference to another function we don't use parenthesis
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_on = True
while game_on:
    # update the screen
    screen.update()
    # sleep
    time.sleep(0.1)  
    # for snake to move smoothly we have to move segments in reverse order
    snake.move_snake()
    
    
    
    
screen.exitonclick()