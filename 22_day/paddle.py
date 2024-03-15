from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x):
        super().__init__('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.penup()
        self.goto(x, 0)

    def up(self):
        if self.ycor() < 230:
            self.goto(self.xcor(), self.ycor() + 20)
            return True
        return False

    def down(self):
        if self.ycor() > -225:
            self.goto(self.xcor(), self.ycor() - 20)
            return True
        return False

