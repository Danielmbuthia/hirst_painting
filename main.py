import turtle as t
import random

# got from RandomColor class
from random_color import RandomColor

color_list = RandomColor().choose_color()

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
