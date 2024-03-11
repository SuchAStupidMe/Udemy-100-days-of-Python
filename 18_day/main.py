import turtle
import random
import colorgram
from colorgram.colorgram import Rgb


def get_color(rgb):
    return rgb.r, rgb.g, rgb.b


def draw_painting(timmy, spacing):
    row = 0
    for _ in range(10):
        for _ in range(10):
            timmy.dot(int(spacing / 2), random.choice(rgb_colors))
            timmy.penup()
            timmy.forward(spacing)
        row += spacing
        timmy.goto(0, row)


colors = [Rgb(r=213, g=154, b=96),
          Rgb(r=52, g=107, b=132),
          Rgb(r=179, g=77, b=31),
          Rgb(r=202, g=142, b=31),
          Rgb(r=115, g=155, b=171),
          Rgb(r=124, g=79, b=99),
          Rgb(r=122, g=175, b=156),]

rgb_colors = [get_color(rgb) for rgb in colors]

screen = turtle.Screen()
screen.screensize(400, 300)
screen.colormode(255)

timmy = turtle.Turtle()
timmy.shape('turtle')
timmy.color('green')


draw_painting(timmy, 30)


screen.exitonclick()






