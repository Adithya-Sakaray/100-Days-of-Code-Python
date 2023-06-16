import colorgram
import turtle as t
import random as rand


my_turtle = t.Turtle()
t.colormode(255)
my_turtle.shape("turtle")
my_turtle.speed("fast")

#extracting colors from the image
color = (colorgram.extract("hirst.jpg",30))
color_list = []

#converting into the required format
for i in range(2,len(color)):
    rgb_data = color[i].rgb
    r = rgb_data.r
    g = rgb_data.g
    b = rgb_data.b
    tup = (r,g,b)
    color_list.append(tup)


def draw_hirst(width):
    sq = 10*10
    my_turtle.penup()
    my_turtle.hideturtle()
    my_turtle.setpos(-sq,-sq)

    for i in range(10):
        my_turtle.setpos(-sq,(-sq )+ (i*2*width))
        for _ in range(10):
            my_turtle.pendown()
            my_turtle.dot(width,rand.choice(color_list))
            my_turtle.penup()
            my_turtle.forward(2*width)

w = int(input("Enter the width of the dot:"))
draw_hirst(w)


screen = t.Screen()
screen.exitonclick()

