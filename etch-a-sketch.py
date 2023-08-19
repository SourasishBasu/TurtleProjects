import turtle as t

#### ---- Etch-A-Sketch ---- ####

t.colormode(255)
tim = t.Turtle()
screen = t.Screen()

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

screen.exitonclick()
