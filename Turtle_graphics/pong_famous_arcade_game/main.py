from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
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
ball = Ball()
     
        
# keybiard settings
screen.listen()
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")

# main code game
game_on = True
while game_on:
    # make the ball move slow
    time.sleep(0.1)
    # update manually
    # when u use tracer u have to manually update the screen
    screen.update()
    ball.move()
    
    # detect collision with top wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
        
    # detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

# screen exxit
screen.exitonclick()