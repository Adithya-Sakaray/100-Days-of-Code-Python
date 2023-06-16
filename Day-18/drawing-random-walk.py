import turtle as t
import random


colors = ["light steel blue","steel blue","sea green","lime","dark khaki","yellow","wheat","dark red","purple","magenta","indigo"]
my_turtle = t.Turtle()
t.colormode(255)
my_turtle.shape("turtle")
my_turtle.color("teal")
my_turtle.width(5)
my_turtle.speed("fast")

while(True):
    my_turtle.forward(50)
    angle = 90 * (random.randint(1,4))
    my_turtle.setheading(angle)
    red = random.randint(1,255)
    green = random.randint(1,255)
    blue = random.randint(1,255)
    my_turtle.pencolor((red,green,blue))


screen = Screen()
screen.exitonclick()
