import random
from turtle import Turtle
class Food(Turtle):
    def __init__(self):
        # inheriting everything from the turtle class
        super().__init__()
        self.food = Turtle()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        
    def refresh(self):
        self.goto(random.randint(-280,280),random.randint(-280,280))