from turtle import Turtle

FONT = ('Courier', 22, 'normal')
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100,270)
        self.write(self.l_score,align="center",font=FONT)
        self.goto(100,270)
        self.write(self.r_score,align="center",font=FONT)

    def left_score(self):
        self.l_score += 1
        self.update_score()

    def right_score(self):
        self.r_score += 1
        self.update_score()
