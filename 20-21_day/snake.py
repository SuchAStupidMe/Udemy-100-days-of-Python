from turtle import Turtle


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for x in range(3):
            self.add_segment(x)

    def move(self):
        for segment_num in range(len(self.snake_body)-1, 0, -1):
            self.snake_body[segment_num].goto(self.snake_body[segment_num - 1].pos())
        self.head.forward(20)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def check_walls(self):
        if abs(self.head.pos()[0]) == 300 or abs(self.head.pos()[1]) == 300:
            return False
        return True

    def extend_snake(self):
        self.add_segment(self.snake_body[-1].position())

    def add_segment(self, x):
        segment = Turtle('square')
        segment.color('white')
        segment.penup()
        segment.goto(x * -20, 0)
        self.snake_body.append(segment)
