from turtle import Turtle
# creating a class for score board 
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.hideturtle()
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.update_scoreboard()        
    # function to increase the score
    def increase_score(self):
        self.score += 1
        # clear method clear and update
        # otherwise the updated score will overlap
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"score: {self.score} High Score: {self.high_score}",align="center",font=("Arial",24,"normal"))
        
    # game over function
    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()
    
