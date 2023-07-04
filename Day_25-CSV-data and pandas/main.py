import turtle
import pandas

screen=turtle.Screen()
screen.title("U.S. State Games")
image="C:/Users/Ashlesha/Documents/Projects/Python Projects #100DaysOfCode/Day_25-CSV-data and pandas/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
guessed_states=[]

while len(guessed_states)<50:
    answer_state=screen.textinput(title="Guess the state",prompt="What's another state's name?").title()

    if answer_state=="Exit":
        missing_states=[]
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrme(missing_states)
        new_data.to_csv("States_to_learn.csv")
        break
    if answer_state in all_states:
        t=turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data=data[data.state==answer_state]
        t.goto(int(state_data.x),int(state_data.y))
        t.write(answer_state)

screen.exitonclick()