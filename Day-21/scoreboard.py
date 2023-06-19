from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Arial",14,"normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.goto(y=275,x=0)
        self.color("white")

    def display_score(self):
        self.clear()
        self.write(f"Score: {self.score}",align=ALIGNMENT,font=FONT)

    def update_score(self):
        self.score += 1 
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align=ALIGNMENT,font=FONT)

