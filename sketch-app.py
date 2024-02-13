import turtle
from turtle import Turtle,Screen

tim = Turtle()
screen = Screen()


def move_forward():
    #tim.setheading(90)
    tim.forward(10)


def move_backwards():
    #tim.setheading(270)
    tim.backward(10)


def clock_wise():
    tim.setheading(tim.heading() + 10)



def counter_clock_wise():
    tim.setheading(tim.heading() - 10)

def clear_drawing():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

# def move_up():
#     tim.setheading(0)
#     tim.forward(10)
#
# def move_down():
#     tim.setheading(180)
#     tim.forward(10)


screen.listen()
screen.onkey(key="w",fun=move_forward)
screen.onkey(key="s",fun=move_backwards)
screen.onkey(key="a",fun=counter_clock_wise)
screen.onkey(key="d",fun=clock_wise)
screen.onkey(key="c",fun=clear_drawing)
screen.exitonclick()