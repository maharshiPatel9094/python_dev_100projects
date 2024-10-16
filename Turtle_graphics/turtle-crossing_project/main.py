import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


# player object
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(player.move_up,"Up")
screen.onkey(player.move_down,"Down")

# main code 
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_cars()
    car_manager.move_cars_x()

    # detect collision with car
    for car in car_manager.all_cars:
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()
            print("Collision detected! Game Over")
    
    #detect successful crossing
    if player.cross_success():
        player.reset_position()
        car_manager.level_up()
        scoreboard.increase_level()

screen.exitonclick()