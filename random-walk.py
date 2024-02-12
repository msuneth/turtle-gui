import turtle as t
import random

tim = t.Turtle()

########### Challenge 4 - Random Walk ########
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
tim.speed(0)
t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_random_step(color):
    tim.color(color)
    tim.width(5)
    angle = [0, 90, 180, 270]
    tim.setheading(random.choice(angle))
    tim.forward(10)


# while True:
#     draw_random_step(random_color())

def draw_spirograph(size_of_tilt):
    for _ in range(int(360 / size_of_tilt)):
        tim.color(random_color())
        tim.circle(50)
        tim.setheading(tim.heading() + size_of_tilt)
        # tim.tilt(10)


draw_spirograph(5)


screen = t.Screen()
screen.exitonclick()
