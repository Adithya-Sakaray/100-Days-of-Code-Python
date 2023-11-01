from turtle import Turtle, Screen
from boundary import Boundary
from player import Player
from laserplayer import LaserPlayer
from laser_enemy import LaserEnemy
from enemy import Enemy
from scoreboard import Scoreboard
import time
import random
from functools import partial
import random

screen = Screen()
screen.setup(height=700, width=600)
screen.bgcolor("black")
screen.title("Space Invaders")
screen.register_shape("Media/player.gif")
screen.register_shape("Media/invader.gif")
screen.tracer(0)

boundary = Boundary()
boundary.draw_boundary()
player = Player()
laser_player = LaserPlayer()
enemy = Enemy()
enemy.create_enemies()
laser_enemy = LaserEnemy()
scoreboard = Scoreboard()

scoreboard.update_scoreboard()
screen.update()


def create_laser():
    x = player.xcor()
    laser_player.create_laser(x)


screen.listen()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")
screen.onkey(create_laser, "space")

game_is_on = True

while game_is_on:

    screen.update()

    # laser and enemy movement
    if laser_player.lasers:
        laser_player.move_forward()
    if laser_enemy.lasers:
        laser_enemy.move_backward()
    enemy.move_enemy()

    # toggle enemy movement direction
    if enemy.enemies:
        for item in enemy.enemies:
            if item.xcor() > 270 or item.xcor() < -270:
                enemy.change_direction()
    else:
        enemy.create_enemies()

    # random shooting
    num = random.randint(0, 10)
    if num == 0:
        rand_enemy = random.choice(enemy.enemies)
        rand_enemy_x = rand_enemy.xcor()
        rand_enemy_y = rand_enemy.ycor()
        laser_enemy.create_laser(rand_enemy_x, rand_enemy_y)

    # if enemy laser strikes the player
    for item in laser_enemy.lasers:
        if item.distance(player) < 10:
            scoreboard.game_over()
            game_is_on = False

    # if laser strikes the enemy
    for l in laser_player.lasers:
        for e in enemy.enemies:
            if l.distance(e) < 20:
                l.hideturtle()
                e.hideturtle()
                laser_player.lasers.remove(l)
                enemy.enemies.remove(e)
                scoreboard.increase_score()
                scoreboard.update_scoreboard()

    time.sleep(0.1)

screen.mainloop()
