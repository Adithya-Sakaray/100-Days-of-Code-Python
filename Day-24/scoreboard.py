from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 14, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.hideturtle()
        self.goto(y=275, x=0)
        self.color("white")

    def display_score(self):
        self.clear()
        with open("highscore.txt",mode="r") as file:
            filescore = file.read()

        self.write(f"Score: {self.score}  High Score: {filescore}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt",mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.display_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER",align=ALIGNMENT,font=FONT)
