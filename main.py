import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
level = Scoreboard()

car_manager = CarManager()
car_manager.gen_cars()

screen.onkeypress(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.move()

    if player.at_finish():
        car_manager.level_up()
        player.level_up()
        level.level_up()

    for car in car_manager.car_list:
        if player.distance(car) < 20:
            level.game_over()
            game_is_on = False

screen.exitonclick()
