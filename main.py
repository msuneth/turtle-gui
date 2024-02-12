#####Turtle Intro######

from turtle import Turtle, Screen
import time

tim = Turtle()
# tim.shape("turtle")
# tim.color("red")

# for _ in range(4):
#     tim.forward(200)
#     tim.right(90)

# for _ in range(20):
#     tim.pendown()
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)


def draw_shape(num_of_sides):
    for n in range(num_of_sides):
        tim.forward(50)
        tim.right(angle)


for sides in range(3, 11):
    angle = 360 / sides
    tim.home()
    draw_shape(sides)




# timmy_the_turtle.right(90)
# time.sleep(1)
#
# timmy_the_turtle.left(180)
# time.sleep(1)
# timmy_the_turtle.forward(100)
# time.sleep(1)
# tim.setheading(0)



######## Challenge 1 - Draw a Square ############