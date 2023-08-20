from turtle import Turtle
FONT=("Courier", 21, "bold")
ALIGNMENT="center"

class Score(Turtle):

    def __init__(self, name, position):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(position)
        self.pendown()
        self.write(f"{name}: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update(name)

    def update(self, name):
        self.write(f"{name}: {self.score}", align=ALIGNMENT, font=FONT)

    def score_up(self, name):
        self.score +=1
        self.clear()
        self.update(name)
