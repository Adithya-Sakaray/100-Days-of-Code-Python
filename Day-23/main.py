import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_forwards, "Up")
screen.onkey(player.move_backwards, "Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    # turtle crashed with obstacle
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # turtle has reached the finish line
    if player.has_reached_finish_line():
        scoreboard.increase_level()
        scoreboard.update_scoreboard()
        player.go_to_start()
        car_manager.increase_speed()

screen.exitonclick()
