from turtle import Turtle


class LaserPlayer(Turtle):

    def __init__(self):
        super().__init__()
        self.lasers = []

    def create_laser(self, x):

        laser = Turtle()
        laser.penup()
        laser.shape("triangle")
        laser.color("yellow")
        laser.shapesize(stretch_wid=0.5, stretch_len=0.5)
        laser.goto(x, -300)
        laser.left(90)
        self.lasers.append(laser)
        self.move_forward()

    def move_forward(self):
        for laser in self.lasers:
            laser.forward(20)
