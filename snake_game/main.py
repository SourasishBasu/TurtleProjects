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
