import colorgram
import turtle as t
import random

def extract_colors(picture, num_of_colors):
    list_of_colors = []
    color_objects = colorgram.extract(picture, num_of_colors)
    for color in color_objects:
        rgb_tuple = (color.rgb[0],color.rgb[1],color.rgb[2])
        list_of_colors.append(rgb_tuple)
    return list_of_colors


color_list = extract_colors("tree-736885_1280.jpg",500)

turtle = t.Turtle()
turtle.speed(0)
t.colormode(255)
turtle.width(5)
turtle.penup()
x_point = -100
y_point = -50
#turtle.setposition(x_point,y_point)

for _ in range(10):
    turtle.setposition(x_point, y_point)
    for _ in range(10):
        turtle.color(random.choice(color_list))
        turtle.pendown()
        turtle.dot()
        turtle.penup()
        turtle.forward(20)
        y_point += 2

screen = t.Screen()
screen.exitonclick()
