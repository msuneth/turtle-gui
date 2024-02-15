import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
tim = Player()
car_list = []
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(tim.move_up, "Up")

game_is_on = True
sleep_time = 0.1
while game_is_on:
    time.sleep(sleep_time)
    car_manager.create_car()
    car_manager.move_cars()
    screen.update()

    for car in car_manager.all_cars:
        if car.distance(tim) < 25:
            score_board.game_over()
            game_is_on = False

    if tim.is_at_finishline():
        car_manager.level_up()
        score_board.update_score()
        score_board.level_up()



screen.exitonclick()
