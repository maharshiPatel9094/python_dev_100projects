from turtle import Turtle
# creating a class for score board 
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.write(arg=f"score: {self.score}",align="center",font=("Arial",24,"normal"))
        
    # function to increase the score
    def increase_score(self):
        self.score += 1
        # clear method clear and update
        # otherwise the updated score will overlap
        self.clear()
        self.write(arg=f"score: {self.score}",align="center",font=("Arial",24,"normal"))
        
    # game over function
    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over",align="center",font=("Arial",24,"normal"))
        