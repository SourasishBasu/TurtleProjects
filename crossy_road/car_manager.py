from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.carspeed = STARTING_MOVE_DISTANCE
    # Creating 3 individual snake objects and placing them to look like they are one object
    def add_car(self):
        chance = random.randint(1,6)
        if chance == 1:
            car = Turtle("square")
            car.shapesize(stretch_len=2, stretch_wid=1)
            car.color(random.choice(COLORS))
            car.penup()
            car.goto(300, random.randint(-230,250))
            self.all_cars.append(car)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.carspeed)


