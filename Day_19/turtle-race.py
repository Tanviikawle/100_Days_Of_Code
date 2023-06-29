from turtle import Turtle,Screen
import random

is_race=False
screen=Screen()
screen.setup(width=500,height=400)

colors=["red","orange","yellow","green","blue","purple"]
y_position=[-70,-40,-10,20,50,80]
all_turtles=[]

user_bet=screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

for turtle in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(colors[turtle])
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_position[turtle])
    all_turtles.append(new_turtle)

if user_bet:
    is_race=True

while is_race:

    for turtle in all_turtles:
        if turtle.xcor()>230:
            is_race=False
            winner=turtle.pencolor()
            if winner==user_bet:
                print(f"You've won! The {winner} turtle is the winner")
            else:
                print(f"You've lost! The {winner} turtle is the winner.")

        rand_distance=random.randint(0,10)
        turtle.forward(rand_distance)

screen.exitonclick()