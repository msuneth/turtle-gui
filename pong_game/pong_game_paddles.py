from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        #self.screen = Screen()
        self.shape("square")
        self.position = position
        self.color("white")
        #self.hideturtle()
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)
        #self.screen.update()

    def go_up(self):
        y_cor = self.ycor() + 20
        self.goto(self.position[0], y_cor)
        #self.screen.update()

    def go_down(self):
        y_cor = self.ycor() - 20
        self.goto(self.position[0], y_cor)
        #self.screen.update()
