from turtle import Turtle

class LaserEnemy(Turtle):

    def __init__(self):
        super().__init__()
        self.lasers = []

    def create_laser(self, x, y):

        laser = Turtle()
        laser.penup()
        laser.shape("triangle")
        laser.color("red")
        laser.shapesize(stretch_wid=0.5, stretch_len=0.5)
        laser.goto(x, y)
        laser.right(90)
        self.lasers.append(laser)
        self.move_backward()

    def move_backward(self):
        for laser in self.lasers:
            laser.forward(20)
