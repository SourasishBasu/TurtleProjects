from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 21, "normal")
# Inherit turtle class in Food class to create and place food object everytime it is called in main file
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.highscore = 0
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.pendown()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update()

    def score_increase(self):
        self.score += 1
        self.update()



