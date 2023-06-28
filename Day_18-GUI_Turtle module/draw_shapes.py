from turtle import Turtle

timmy=Turtle()

side=3

while side<=10:
    # timmy.pencolor(make_color())
    for i in range(side):
        timmy.forward(100)
        timmy.right(360/side)
    side+=1