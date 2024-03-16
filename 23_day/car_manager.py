from turtle import Turtle
from random import randint, choice

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.cars_list = []

    def create_car(self):
        if len(self.cars_list) < 20:
            car = Car()
            self.cars_list.append(car)

    def move_cars(self):
        for car in self.cars_list:
            car.move()

    def increase_speed(self):
        for car in self.cars_list:
            car.move_speed += MOVE_INCREMENT


class Car(Turtle):
    def __init__(self):
        super().__init__('square')
        self.color(choice(COLORS))
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.move_speed = STARTING_MOVE_DISTANCE
        self.penup()
        self.start()

    def start(self):
        self.goto(320, randint(-250, 250))

    def move(self):
        if self.xcor() > -320:
            self.goto(self.xcor() - self.move_speed, self.ycor())
        else:
            self.start()

    def detect_collision(self, turtle):
        if self.distance(turtle) < 20:
            return True
        return False
