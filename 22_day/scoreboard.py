from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self, align, x_cor):
        super().__init__()
        self.align = align
        self.score = 0
        self.hideturtle()
        self.penup()
        self.color('white')
        self.goto(x_cor, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.score}", align=self.align, font=('Courier', 20, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align='center', font=('Courier', 24, 'normal'))