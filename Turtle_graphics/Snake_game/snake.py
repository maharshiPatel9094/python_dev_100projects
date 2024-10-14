# snake class
from turtle import Turtle,Screen
import time
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20  


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head  = self.segments[0]

        
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            segment = Turtle("square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)
    
    def move_snake(self):
            for seg_num in range(len(self.segments)-1,0,-1):
                new_x = self.segments[seg_num - 1].xcor()
                new_y = self.segments[seg_num - 1].ycor()
                self.segments[seg_num].goto(new_x,new_y)
            self.head.forward(MOVE_DISTANCE)
    
    def up(self):
        if  self.head.heading() != 270:
            self.head.setheading(90)
    
    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)
    
    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
    
    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)
        