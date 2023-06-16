import turtle as t
import random as rand

my_turtle = t.Turtle()
t.colormode(255)
my_turtle.shape("turtle")
my_turtle.color("teal")
my_turtle.width(2)
my_turtle.speed("fastest")

def random_color():
    r = rand.randint(1,255)
    g = rand.randint(1,255)
    b = rand.randint(1,255)
    color = (r,g,b)
    return color

def draw_spirograph(size_of_width):
    
    limit = int((360/size_of_width) + 1)
    for _ in range(1,limit):
        my_turtle.color(random_color())
        my_turtle.circle(75)
        my_turtle.setheading(my_turtle.heading() + size_of_width)

w = int(input("Enter the width:"))
draw_spirograph(w)
    

screen = t.Screen()
screen.exitonclick()
