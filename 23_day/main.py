# Turtle Crossing
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkey(player.move, 'w')
scoreboard = Scoreboard()

cars = CarManager()

frame = 0
game_is_on = True
while game_is_on:
    if player.finish():
        scoreboard.increase_level()
        cars.increase_speed()

    for car in cars.cars_list:
        if car.distance(player) < 50:
            if car.detect_collision(player):
                scoreboard.game_over()
                game_is_on = False
    if frame == 6:
        cars.create_car()
        frame = 0
    else:
        frame += 1

    cars.move_cars()
    time.sleep(0.1)
    screen.update()

screen.exitonclick()
