import random
# from typing import Counter
from game_data import data
from art import logo, vs
import os

def get_account():
    return random.choice(data)

def print_format(account):
    name=account["name"]
    desc=account["description"]
    country=["country"]
    return (f"{name}, a {desc} from {country}.")

def compare(num1,num2):
    if num1>num2:
        return num1
    else:
        return num2

score=0
opt_a=get_account()
opt_b=get_account()
game_on=True
print(logo)
while game_on:
    opt_a=opt_b
    opt_b=get_account()
    if opt_a==opt_b:
        opt_b=get_account()
        
    str_a=print_format(opt_a)
    print(f"Compare A:{str_a}")
    print(vs)
    str_b=print_format(opt_b)
    print(f"Compare A:{str_b}")

    followers_a=opt_a['follower_count']
    followers_b=opt_a['follower_count']
    result=compare(followers_a,followers_b)
    if result==followers_a:
        answer="a"
    else:
        answer="b"

    user_guess=input("Which one has more instagram followers? Type 'A' or 'B': ").lower()

    os.system('cls')
    print(logo)

    if user_guess==answer:
        score+=1
        print(f"You are correct. Current score: {score}.")
    else:
        print(f"Oops! That's wrong. Final score: {score}.")
        game_on=False
    






    







