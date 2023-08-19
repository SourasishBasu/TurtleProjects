import turtle as t

MOVE_DISTANCE=20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
STARTINGPOSITIONS = [(0,0),(-20,0),(-40,0)]
class Snake:

    def __init__(self):
        self.segments = []
        self.create_snek()
        self.head = self.segments[0]

    # Creating 3 individual snake objects and placing them to look like they are one object
    def create_snek(self):
        for position in STARTINGPOSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snek = t.Turtle(shape="square")
        snek.color("white")
        snek.penup()
        snek.goto(position)
        self.segments.append(snek)

    # Grow snake size by 1 snake object when food object encountered
    def grow(self):
        self.segments.append(self.segments[-1].position())


    # Movement Controls preventing snake object to go back the same direction it came from instantly and collide onto itself
    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # Moving the snake object cohesively
    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg - 1].xcor()
            new_y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)


