from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 12, 'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.shape("blank")
        self.penup()
        self.hideturtle()
        self.goto(0,280)
        self.score_update(self.score)

    def score_update(self, score):
        self.score += score
        self.clear()
        self.write(f"Score: {self.score}",
                   False, align=ALIGNMENT,
                   font=FONT)
        print(f"score updated to {self.score}")

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",
                   False, align=ALIGNMENT,
                   font=FONT)
