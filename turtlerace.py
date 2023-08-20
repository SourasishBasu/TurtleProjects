import turtle as t
from turtle import Screen
import random
#### ---- Turtle Race ---- ####
screen = Screen()
screen.bgcolor("grey")
screen.setup(width=500, height=400)

y = [100, 50, 0, -50, -100]
colors = ["red", "green", "blue", "orange", "purple"]

user_bet = screen.textinput(title="Enter bet.", prompt="Which turtle will win the race? Enter color: ")
all_turtles = []


def move(turt):
    steps = random.randint(0, 10)
    turt.forward(steps)


for i in range(0, 5):
    tim = t.Turtle(shape="turtle")
    tim.color(colors[i])
    tim.penup()
    tim.setposition(-230, y[i])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True


while is_race_on:
    for turt in all_turtles:
        if turt.xcor() > 230:
            is_race_on = False
            win = turt.pencolor()
            if win == user_bet:
                print(f"You've won. {win.title()} turtle won. ")
            else:
                print(f"You've lost. {win.title()} turtle won. ")

        move(turt)

screen.exitonclick()
