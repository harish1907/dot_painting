# from colorgram import *
#
# colors = extract('image.jpg', 35)
# rgb_color = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_color.append(new_color)
# print(rgb_color)
import turtle as t
import random

my_screen = t.Screen()
colors = [(58, 106, 147), (225, 201, 110), (133, 82, 58), (223, 136, 61), (196, 145, 171), (235, 226, 203),
          (223, 233, 229), (143, 179, 203), (139, 82, 105), (208, 90, 70), (134, 133, 75), (136, 182, 138),
          (69, 105, 92), (237, 224, 232), (187, 81, 120), (65, 156, 91), (49, 156, 194), (183, 192, 201),
          (215, 176, 191), (19, 58, 92), (24, 67, 111), (166, 202, 209), (227, 176, 165), (176, 202, 181),
          (113, 123, 148), (69, 57, 46), (75, 66, 48), (111, 45, 55), (121, 44, 41), (44, 79, 73), (22, 80, 101),
          (49, 67, 61), (79, 43, 55)]

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.hideturtle()

tim.setheading(225)
tim.penup()
tim.forward(360)
tim.pendown()
tim.setheading(0)
num_of_dots = 100

for i in range(1, num_of_dots + 1):
    tim.dot(20, random.choice(colors))
    tim.penup()
    tim.forward(50)
    tim.pendown()

    if i % 10 == 0:
        tim.setheading(90)
        tim.penup()
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.pendown()
        tim.setheading(0)

my_screen.exitonclick()
