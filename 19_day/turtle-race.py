# Turtle Race
from turtle import Turtle, Screen
from random import randint


screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race? Enter a color: ')

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtles = []
for x in colors:
    turtle = Turtle('turtle')
    turtle.color(x)
    turtle.penup()
    turtle.goto((-230, colors.index(x) * 30))
    turtle.speed(10)
    turtles.append(turtle)

race_ended = False
winner = None
while not race_ended:
    for turtle in turtles:
        turtle.forward(randint(0, 10))
        if turtle.pos()[0] > 230:
            race_ended = True
            winner = turtles.index(turtle)


if user_bet == colors[winner]:
    print(f"Congrats! {colors[winner].capitalize()} turtle is a winner.")
else:
    print(f"{colors[winner].capitalize()} turtle is a winner. You lost.")

screen.exitonclick()
