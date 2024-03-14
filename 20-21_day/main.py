# Snake Game
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from time import sleep
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title("Snake Game")


snake = Snake()
food = Food()
screen.update()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'w')
screen.onkey(snake.down, 's')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')

game_is_on = True
while game_is_on:
    snake.move()
    screen.update()
    sleep(0.2)

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend_snake()
        scoreboard.increase_score()

    if not snake.check_walls():
        game_is_on = False

    for segment in snake.snake_body[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False


scoreboard.game_over()
screen.exitonclick()
