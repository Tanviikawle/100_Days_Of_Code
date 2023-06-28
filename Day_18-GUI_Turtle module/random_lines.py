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

directions=[0,90,180,270]
timmy.pensize(10)
timmy.speed("fastest")

# timmy.setheading(random.choice(directions))

for i in range(100):
    timmy.color(make_color())
    timmy.setheading(random.choice(directions))
    timmy.forward(15)