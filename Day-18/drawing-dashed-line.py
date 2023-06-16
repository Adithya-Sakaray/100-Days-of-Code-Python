from turtle import Turtle,Screen

my_turtle = Turtle()

my_turtle.shape("turtle")
my_turtle.color("teal")

for _ in range(50):
    my_turtle.forward(5)
    my_turtle.penup()
    my_turtle.forward(5)
    my_turtle.pendown()


my_screen = Screen()
my_screen.exitonclick()
