from turtle import Screen
from paddle import Paddle
from score import Score
from ball import Ball
import time

# Player Name Input
lname = input("Enter left player name: ")
rname = input("Enter right player name: ")

# Initializing Game Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("My Pong Game")
screen.tracer(0)


# Initialize paddles and pass position coords as tuples
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

# Setup Score and Ball
l_score = Score(lname, (-150,270))
r_score = Score(rname, (150,270))
ball = Ball()

# Checking for keypress event
screen.listen()
screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

# Running Game
game_on = True

while game_on:
    # Delaying screen refresh time and increasing ball update speed on paddle collision
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Check for collision with top and bottom bounds
    if ball.ycor() < -280 or ball.ycor() > 280:
        ball.bounce_y()

    # Check for collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Check for ball going out of bounds for either players
    if ball.xcor() > 390:
        ball.reset_pos()
        l_score.score_up(lname)

    elif ball.xcor() < -390:
        ball.reset_pos()
        r_score.score_up(rname)

screen.exitonclick()
