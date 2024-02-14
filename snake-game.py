from turtle import Screen
import time
from snake import Snake
from snake_food import Food
from snake_scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()

    if snake.head.distance(food) < 15:
        scoreboard.score_update(1)
        snake.extend()
        food.refresh_location()

    if snake.head.xcor() < -280 or snake.head.xcor() > 280 or snake.head.ycor() < -280 or snake.head.xcor() > 280:
        scoreboard.game_over()
        game_is_on = False

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.game_over()
            game_is_on = False



# def snake(size):
#     x_shift = 0
#     for n in range(size):
#         t = Turtle("square")
#         t.penup()
#         t.color("white")
#         t.goto(x_shift,0)
#         x_shift += 20
#         #snake_positions.append((t.xcor(), t.ycor()))
#         snake_positions.append(t)
#     screen.update()
#
#
# def move_forward(steps,snake_positions_list):
#     for sn in snake_positions:
#         sn.forward(steps)
#     time.sleep(0.1)
#     screen.update()
#
#
# snake(5)
# change_direction = False
# while not change_direction:
#     move_forward(10,snake_positions)
#
#
#
# screen.listen()
# screen.onkey(key="w",fun=move_forward)
screen.exitonclick()
