from turtle import Screen
from pong_game.pong_game_paddles import Paddle
from pong_game.pong_game_ball import Ball
from pong_game.pong_game_scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
score_board = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

sleep_time = 0.1
game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    ball.move_ball()

    # detect collision
    if ball.ycor() == -290 or ball.ycor() == 290:
        ball.bounce_y()

    if ball.xcor() == 330 and ball.distance(r_paddle) < 50 or ball.xcor() == -330 and ball.distance(l_paddle) < 50:
        ball.bounce_x()

    if ball.xcor() == 390:
        score_board.left_score()
        ball.reset_position()

    if ball.xcor() == -390:
        score_board.right_score()
        ball.reset_position()

    screen.update()

screen.exitonclick()
