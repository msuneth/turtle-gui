from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 12, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highest_score = 0
        self.get_highest_score_from_file()
        self.color("white")
        self.shape("blank")
        self.penup()
        self.hideturtle()
        self.score_update()

    def get_highest_score_from_file(self):
        with open("snake_game/highest_score.txt") as file:
            self.highest_score = int(file.read())

    def set_highest_score_to_file(self):
        with open("snake_game/highest_score.txt","w") as file:
            file.write(str(self.highest_score))

    def score_increase(self):
        self.score += 1
        self.score_update()

    def score_update(self):
        self.goto(-100, 280)
        self.clear()
        if self.score > self.highest_score:
            self.highest_score = self.score
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 280)
        self.write(f"Highest Score: {self.highest_score}", align=ALIGNMENT, font=FONT)
        self.set_highest_score_to_file()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def reset_scores(self):
        self.score = 0
        self.score_update()


