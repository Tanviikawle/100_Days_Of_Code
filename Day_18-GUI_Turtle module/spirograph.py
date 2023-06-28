import turtle as t
import random

timmy=t.Turtle()
# timmy.colormode(255)
t.colormode(255)

def make_color():
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    random_color=(r,g,b)
    return random_color

timmy.speed("fastest")

def spiral(size_of_gap):
    for i in range(int(360/size_of_gap)):
        timmy.color(make_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading()+size_of_gap)

spiral(5)

screen=t.Screen()
screen.exitonclick()