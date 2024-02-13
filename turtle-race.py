import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=600, height=500)
user_bet = screen.textinput("Make Your bet!", "Which color turtle wins the race?")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
shift = 0
new_turtles = []
is_game_start = False

for col in colors:
    turtle = Turtle(shape="turtle")
    turtle.color(col)
    turtle.penup()
    turtle.goto(x=-230, y=-190 + shift)
    shift += 50
    new_turtles.append(turtle)

if user_bet:
    is_game_start = True

while is_game_start:
    for t in new_turtles:
        if t.xcor() > 250:
            is_game_start = False
            print(t.color()[0])
            if t.color() == user_bet:
                print(f"You've won. The winner is {t.color()[0]}")
            else:
                print(f"You lose. The winner is {t.color()[0]}")
        t.forward(random.randint(0,10))

screen.exitonclick()
