from turtle import Turtle

class BlocksManager():

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.all_blocks = []

    def create_blocks(self):

        colors = ["green", "orange", "red"]
        prev_x = -((self.width//2) - 50)
        prev_y = (self.height//2) - 100
        for i in range(3):
            for j in range(11):
                new_block = Turtle("square")
                new_block.shapesize(stretch_wid=1, stretch_len=3)
                new_block.penup()
                new_block.color(colors[i])
                new_block.goto(prev_x, prev_y)
                self.all_blocks.append(new_block)
                prev_x += 70
            prev_y += 25
            prev_x = -((self.width // 2) - 50)


