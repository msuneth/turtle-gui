from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        # self.screen = Screen()
        self.shape("circle")
        self.color("blue")
        # self.hideturtle()
        # self.shapesize(stretch_wid=20, stretch_len=20)
        self.penup()
        self.goto(0, 0)
        # self.screen.update()
        # self.speed(1)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # def increase_speed(self):
    #     current_speed = self.speed()
    #     self.speed(current_speed + 3)
    #     print(self.speed())

    def move_ball(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        print("ball y bounce")
        self.y_move *= -1

    def bounce_x(self):
        print("ball x bounce")
        self.move_speed *= 0.9
        self.x_move *= -1
        # y_cor = self.ycor() + 20
        # self.goto(self.position[0], y_cor)

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_move *= -1
