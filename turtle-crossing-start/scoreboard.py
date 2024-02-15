from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.score = 0
        self.level = 1
        self.display()

    def display(self):
        self.clear()
        self.goto(100, 270)
        self.write(f"Score: {self.score}", align="center", font=FONT)
        self.goto(-100, 270)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update_score(self):
        self.score += 1
        self.display()

    def level_up(self):
        self.level += 1
        self.display()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

