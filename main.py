import turtle as t
import random

# got from RandomColor class
color_list = [(239, 234, 226), (220, 158, 84), (39, 109, 150), (120, 163, 191), (150, 63, 87), (217, 232, 222),
              (203, 134, 157), (180, 160, 34), (32, 131, 95), (122, 179, 152), (235, 218, 225), (161, 79, 52),
              (213, 87, 61), (197, 85, 112), (208, 223, 231), (229, 199, 114), (57, 166, 135), (141, 33, 42),
              (8, 104, 80), (47, 158, 182), (234, 163, 181), (117, 115, 162), (32, 62, 111), (236, 171, 157),
              (126, 38, 34), (156, 210, 197), (32, 57, 78), (70, 41, 37), (25, 65, 56), (74, 37, 47)]

tim = t.Turtle()
t.colormode(255)
tim.speed("fastest")
tim.penup()
# move the turtle near left corner
tim.setheading(225)
tim.forward(300)
tim.setheading(0)

dot_numbers = 101

for count in range(1, dot_numbers):
    tim.dot(30, random.choice(color_list))  # increase the size to draw different dot size try 100
    tim.forward(50)

    if count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = t.Screen()
screen.exitonclick()
