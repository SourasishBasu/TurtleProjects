import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Score()
car_manager = CarManager()

screen.listen()
screen.onkey(player.move, "w")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()

    car_manager.add_car()
    car_manager.move_car()

    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_on = False
            score.endgame()

    if player.ycor() > 280:
        player.reset_pos()
        car_manager.carspeed += 10
        score.score_increase()


screen.exitonclick()

