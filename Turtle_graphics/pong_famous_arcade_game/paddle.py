# paddle class
from turtle import Turtle,Screen

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color("white")
        self.penup()
        self.shape("square")
        #turtle is 20*20 so 20*5 = 100 , 20*1 = 20 
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.goto(position)
        
    # move up function 
    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)
        
    # move down function
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)