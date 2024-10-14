from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500,height=400)
# show a pop up
user_bet = screen.textinput(title="Make Your Bet",prompt="Which turtle will win the race? Enter a color: ")
# print(user_bet)




colors = ["red","orange","yellow","green","blue","purple"]
y_positions = [-70,-40,-10,20,50,80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    # not 250 bcz it will go to edge and will not be visible
    new_turtle.goto(x=-230,y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)
    
if user_bet:
    is_race_on = True
    
while is_race_on:
    for turtle in all_turtles:
        # turtle size is 40 * 40
        if turtle.xcor() > 230:
            is_race_on = False
            # print(turtle.color())
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        random_turtle_distance = random.randint(0,10)
        turtle.forward(random_turtle_distance)

# screen 
screen.exitonclick()