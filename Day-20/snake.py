from turtle import Turtle

STARTING_POS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        
        for i in range(3):
            new_turtle = Turtle()
            new_turtle.color("white")
            new_turtle.shape("square")
            new_turtle.penup()
            new_turtle.goto(STARTING_POS[i])
            self.segments.append(new_turtle)

    def move_forwards(self):
        for i in range(len(self.segments)-1, 0 , -1):
            new_x = self.segments[i-1].xcor()
            new_y = self.segments[i-1].ycor()
            self.segments[i].goto(new_x,new_y)
    
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)
    
    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(LEFT)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
