from turtle import Turtle


class Enemy(Turtle):

    def __init__(self):

        super().__init__()
        self.enemies = []
        self.forward = True

    def create_enemies(self):

        init_x = -100
        init_y = 100

        for i in range(3):
            for j in range(5):
                enemy = Turtle()
                enemy.penup()
                enemy.shape("Media/invader.gif")
                enemy.setposition(init_x, init_y)
                self.enemies.append(enemy)
                init_x += 50
            init_x = -100
            init_y += 40

    def move_enemy(self):
        for enemy in self.enemies:
            if self.forward:
                enemy.goto(enemy.xcor() + 5, enemy.ycor())
            else:
                enemy.goto(enemy.xcor() - 5, enemy.ycor())

    def change_direction(self):
        if self.forward:
            self.forward = False
        else:
            self.forward = True
