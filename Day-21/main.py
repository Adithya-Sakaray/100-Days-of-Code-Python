from turtle import Screen
from food import Food
from scoreboard import Scoreboard
import time
from snake import Snake
from boundary import Boundary

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

boundary = Boundary()
snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True

boundary.drawboundary()
while game_is_on:

    screen.update()
    time.sleep(0.1)

    scoreboard.display_score()

    snake.move_forwards()

    #detection of collision
    if (snake.head.distance(food) < 15 ):
        food.refresh()
        snake.extend()
        scoreboard.update_score()

    if (snake.head.xcor() >= 295 or snake.head.xcor() <= -295 or snake.head.ycor() >= 295 or snake.head.ycor() <= -295):
        scoreboard.game_over()
        game_is_on = False

    for segment in snake.segments:

        if snake.head == segment:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()


screen.exitonclick()
