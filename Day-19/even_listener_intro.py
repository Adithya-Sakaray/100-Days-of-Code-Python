import turtle as t

my_turtle = t.Turtle()
my_turtle.width(5)
my_turtle.color("teal")

def move_forward():
    my_turtle.forward(10)

def move_right():
    my_turtle.right(5)

def move_left():
    my_turtle.left(5)

def move_backward():
    my_turtle.backward(10)

def clear():
    my_turtle.clear()
    my_turtle.penup()
    my_turtle.home()

screen = t.Screen()
screen.listen()
screen.onkeypress(key="w",fun=move_forward)
screen.onkeypress(key="a",fun=move_left)
screen.onkeypress(key="d",fun=move_right)
screen.onkeypress(key="s",fun=move_backward)
screen.onkeypress(key="c",fun=clear)
screen.exitonclick()