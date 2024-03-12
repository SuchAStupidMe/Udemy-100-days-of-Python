# Etch-A-Sketch
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def rotate_clockwise():
    tim.right(5)


def rotate_counterclockwise():
    tim.left(5)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key='s', fun=move_backwards)
screen.onkey(key='a', fun=rotate_counterclockwise)
screen.onkey(key='d', fun=rotate_clockwise)
screen.onkey(key='space', fun=clear)
screen.exitonclick()
