from turtle import Turtle,Screen
from random import choice  


colors = ["light steel blue","steel blue","sea green","lime","dark khaki","yellow","wheat","dark red","purple","magenta","indigo"]
my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("teal")
my_turtle.width(5)

for sides in range(3,11):

    angle = 360/sides
    my_color = choice(colors)
    my_turtle.color(my_color)
    for _ in range(sides):
        my_turtle.forward(100)
        my_turtle.right(angle)


screen = Screen()
screen.exitonclick()
