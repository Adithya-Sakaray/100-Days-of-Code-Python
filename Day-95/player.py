from turtle import Turtle
from laserplayer import LaserPlayer


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("blue")
        self.shape("Media/player.gif")
        self.setposition(0, -300)

    def move_left(self):
        self.backward(15)

    def move_right(self):
        self.forward(15)





