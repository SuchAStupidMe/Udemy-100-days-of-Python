# Pong Game
from turtle import Screen
from paddle import Paddle
from time import sleep
from ball import Ball
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)


paddle = Paddle(350)
computer_paddle = Paddle(-350)
ball = Ball()
l_score = Scoreboard('left', -200)
r_score = Scoreboard('right', 200)

screen.update()


screen.listen()
screen.onkeypress(paddle.up, 'w')
screen.onkeypress(paddle.down, 's')
screen.onkeypress(computer_paddle.up, 'Up')
screen.onkeypress(computer_paddle.down, 'Down')

game_is_on = True
while game_is_on:
    ball.move()
    if ball.distance(paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        ball.change_speed()
    elif ball.distance(computer_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        ball.change_speed()

    if ball.xcor() > 390:
        ball.reset_position()
        l_score.increase_score()
    elif ball.xcor() < -390:
        ball.reset_position()
        r_score.increase_score()

    screen.update()
    sleep(0.1)


screen.exitonclick()
