from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

# Initializing Game Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


# Initialize snake and food
snake = Snake()
food = Food()
score = Score()

# Checking for keypress event
screen.listen()
screen.onkey(snake.move_left, "a")
screen.onkey(snake.move_right, "d")
screen.onkey(snake.move_down, "s")
screen.onkey(snake.move_up, "w")

# Running Game
game_on = True

while game_on:
    screen.update()
    # Timer to delay the snake object update after movement so that it stays in one piece
    time.sleep(0.1)
    snake.move()

    # Updating score and snake size
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        score.score_increase()

    # Check for collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() < -280 or snake.head.ycor() > 280:
        game_on = False
        score.endgame()

    # Check for collision with tail
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            game_on = False
            score.endgame()

screen.exitonclick()
'''

#### ---- Turtle Race ---- ####

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
       

#### ---- Damien Hirst Spot Painting ---- ####

t.colormode(255)
screen.bgcolor(233,233,233)
tim.speed(0)

color_list=[(207, 161, 84), (54, 89, 131), (145, 91, 39), (139, 26, 49), (222, 206, 109), (133, 176, 202), (46, 55, 102), (156, 47, 82), (170, 158, 40), (129, 188, 142), (82, 20, 43), (36, 43, 69), (185, 93, 106), (186, 139, 168), (84, 123, 180), (58, 39, 30), (78, 152, 163), (87, 156, 91), (194, 78, 72), (161, 201, 219), (45, 74, 77), (79, 73, 44), (58, 126, 123), (218, 176, 186), (220, 182, 168), (171, 206, 171), (179, 188, 211), (49, 73, 72), (138, 39, 37), (44, 63, 62)]

for row in range(10):
    tim.penup()
    tim.hideturtle()
    tim.setposition(-270, (-260 + (row * 60)))

    for turns in range(10):
        tim.dot(30, random.choice(color_list))
        tim.penup()
        tim.forward(60)
        tim.pendown()


#### ---- Etch-A-Sketch ---- ####

def move_forward():
    tim.forward(10)

def move_left():
    new = tim.heading() - 10
    tim.setheading(new)


def move_right():
    new=tim.heading() + 10
    tim.setheading(new)

def move_backward():
    tim.back(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forward, "w")
screen.onkey(move_backward, "s")
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")
screen.onkey(clear, "c")

'''

screen.exitonclick()
