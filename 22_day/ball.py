from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__('square')
        self.color('white')
        self.penup()
        self.x_head = 10
        self.y_head = 10

    def move(self):
        self.goto(self.xcor() + self.x_head, self.ycor() + self.y_head)
        self.detect_floors()

    def detect_floors(self):
        if abs(self.ycor()) > 280:
            self.bounce_y()

    def bounce_y(self):
        self.y_head = -self.y_head

    def bounce_x(self):
        self.x_head = -self.x_head

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()

    def change_speed(self):
        self.x_head += 5
        self.y_head += 5
