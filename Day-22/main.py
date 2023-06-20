from turtle import Turtle,Screen
from ball import Ball
from paddle import Paddle
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.bounce_x()
        scoreboard.r_point()
        
        

    if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.bounce_x()
        scoreboard.l_point()

    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.reset_ball()





screen.exitonclick()