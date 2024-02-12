from turtle import Turtle, Screen


tim = Turtle()


def draw_shape(num_of_sides):
    for n in range(num_of_sides):
        tim.forward(50)
        tim.right(angle)


for sides in range(3, 11):
    angle = 360 / sides
    tim.home()
    draw_shape(sides)


