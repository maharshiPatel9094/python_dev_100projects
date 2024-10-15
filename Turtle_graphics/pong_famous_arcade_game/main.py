from turtle import Turtle,Screen
from paddle import Paddle

# screen setup 
screen = Screen()
screen.title("PONG: The Famous Arcade Game")
screen.setup(width=800, height=600)
screen.bgcolor("black")
# turn off the animation
screen.tracer(0)


# paddle
r_paddle = Paddle((350,0))
l_paddle =  Paddle((-350,0))
     
        
# keybiard settings
screen.listen()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")

# main code game
game_on = True
while game_on:
    # update manually
    # when u use tracer u have to manually update the screen
    screen.update()

# screen exxit
screen.exitonclick()