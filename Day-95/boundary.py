from turtle import Turtle


class Boundary(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.width(5)
        self.pencolor("white")

    def draw_boundary(self):
        self.goto(300, 350)
        self.pendown()
        self.goto(300, -350)
        self.goto(-300, -350)
        self.goto(-300, 350)
        self.goto(300, 350)
        self.penup()
        self.hideturtle()
