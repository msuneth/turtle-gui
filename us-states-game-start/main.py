from turtle import Turtle, Screen
import pandas

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle = Turtle(image)

df = pandas.read_csv("50_states.csv")
all_states = df.state.to_list()
guessed_states = []

while len(guessed_states) <= len(all_states):
    answer_state = screen.textinput(f"{len(guessed_states)}/50 States correct", "Name another State?").title()
    if answer_state == "Exit":
        break
    if answer_state in all_states:
        pin = Turtle("blank")
        pin.hideturtle()
        pin.penup()
        state_info = df[df.state == answer_state]
        pin.goto(int(state_info.x), int(state_info.y))
        print(state_info.items)
        pin.write(answer_state, align="center", font=('Courier', 10, 'normal'))
        guessed_states.append(answer_state)

# missed_states = []
# for state in all_states:
#     if state not in guessed_states:
#         missed_states.append(state)

missed_states = [state for state in all_states if state not in guessed_states]

new_data = pandas.DataFrame(missed_states)
new_data.to_csv("missed_states.csv")



# location = df[df.state == answer_state]
# x_cor = location['x']
# y_cor = location['y']
# print(location)
# print(x_cor,y_cor)

# def get_mouse_click(x, y):
#     print(x, y)
#
# screen.onscreenclick(get_mouse_click)
#screen.mainloop()
# screen.exitonclick()
