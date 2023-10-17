from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from blocks import BlocksManager
from scoreboard import Scoreboard
import time


GAME_SPEED = 0.05
ball = Ball()
paddle = Paddle((0, -250))
block_manager = BlocksManager(800, 600)
scoreboard = Scoreboard()



screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)



screen.listen()
screen.onkey(paddle.go_right, "Right")
screen.onkey(paddle.go_left, "Left")

block_manager.create_blocks()

game_is_on = True

while game_is_on:
    time.sleep(GAME_SPEED)
    ball.move()
    screen.update()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.bounce_x()

    if ball.distance(paddle) < 45 and ball.ycor() < -230:
        ball.bounce_y()

    if ball.ycor() < -250:
        scoreboard.game_over()
        game_is_on = False

    if len(block_manager.all_blocks) == 0:
        block_manager.create_blocks()
        GAME_SPEED *= 0.9

    for block in block_manager.all_blocks:
        if ball.distance(block) < 35:
            ball.bounce_y()
            block.hideturtle()
            block_manager.all_blocks.remove(block)
            scoreboard.increase_score()




screen.exitonclick()
