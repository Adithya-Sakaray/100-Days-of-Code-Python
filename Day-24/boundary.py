from turtle import Turtle

class Boundary(Turtle):

    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.penup()
        self.width(5)
        self.pencolor("white")

    def drawboundary(self):
        self.goto(300,300)
        self.pendown()
        self.goto(300,-300)
        self.goto(-300,-300)
        self.goto(-300,300)
        self.goto(300,300)
        self.penup()
        self.hideturtle()