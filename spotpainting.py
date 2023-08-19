import turtle as t
import random

#### ---- Damien Hirst Spot Painting ---- ####

t.colormode(255)
tim = t.Turtle()
screen = t.Screen()
screen.bgcolor(233,233,233)

# Palette generated using the colorgram library from a Damien Hirst Spot Painting example
color_list=[(207, 161, 84), (54, 89, 131), (145, 91, 39), (139, 26, 49), (222, 206, 109), (133, 176, 202), (46, 55, 102), (156, 47, 82), (170, 158, 40), (129, 188, 142), (82, 20, 43), (36, 43, 69), (185, 93, 106), (186, 139, 168), (84, 123, 180), (58, 39, 30), (78, 152, 163), (87, 156, 91), (194, 78, 72), (161, 201, 219), (45, 74, 77), (79, 73, 44), (58, 126, 123), (218, 176, 186), (220, 182, 168), (171, 206, 171), (179, 188, 211), (49, 73, 72), (138, 39, 37), (44, 63, 62)]
tim.speed(0)

for row in range(10):
    tim.penup()
    tim.hideturtle()
    tim.setposition(-270, (-260 + (row * 60)))

    for turns in range(10):
        tim.dot(30, random.choice(color_list))
        tim.penup()
        tim.forward(60)
        tim.pendown()

screen.exitonclick()