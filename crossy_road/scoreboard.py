from turtle import Turtle
ALIGNMENT = "left"
FONT = ("Courier", 21, "bold")

# Inherit turtle class in Food class to create and place food object everytime it is called in main file
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-280, 260)
        self.pendown()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)

    def score_increase(self):
        self.level += 1
        self.clear()
        self.update()

    def endgame(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align=ALIGNMENT, font=FONT)
