# Snake Game
import time
from turtle import Turtle, Screen


class Snake:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=600, height=600)
        self.screen.bgcolor('black')
        self.screen.tracer(0)
        self.screen.title("Snake Game")
        self.screen.listen()
        self.screen.onkey(self.up, 'w')
        self.screen.onkey(self.down, 's')
        self.screen.onkey(self.left, 'a')
        self.screen.onkey(self.right, 'd')

        self.snake_body = []
        for x in range(3):
            segment = Turtle('square')
            segment.color('white')
            segment.penup()
            segment.goto(x * -20, 0)
            self.snake_body.append(segment)
        self.screen.update()

        self.head = self.snake_body[0]

    def move(self):
        for segment_num in range(len(self.snake_body)-1, 0, -1):
            self.snake_body[segment_num].goto(self.snake_body[segment_num - 1].pos())
        self.head.forward(20)
        self.screen.update()
        time.sleep(0.2)

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
        if abs(self.snake_body[0].pos()[0]) == 300 or abs(self.snake_body[0].pos()[1]) == 300:
            return False
        return True


snake = Snake()

game_is_on = True
while snake.check_walls():
    snake.move()


snake.screen.exitonclick()
