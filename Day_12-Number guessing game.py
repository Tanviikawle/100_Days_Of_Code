import random

print("Welcome to Number guessing game!\nI'm thinking of number between 1 to 100.")

EASY_LEVEL=10
HARD_LEVEL=5

def set_difficulty(level):
    if level=="easy":
        return EASY_LEVEL
    elif level=="hard":
        return HARD_LEVEL
    else:
        print("Invalid input!")


num=random.randint(1,100)
level=input("Choose difficuty.Type 'easy' or 'hard': ")
guesses=set_difficulty(level)

# print(num)

game_on=True

while game_on:
    if guesses!=0:
        print(f"You've {guesses} attempts remaining to guess the number.")
        guess_made = int(input("Make a guess: "))
        if guess_made==num:
            print("You guessed it right!")
            guesses=0
            game_on=False
        elif guess_made>num:
            print("Too high.\nGuess again.")
            guesses-=1
        elif guess_made<num:
            print("Too low.\nGuess again.")
            guesses-=1
        else:
            print("Invalid input.\nEnter number for guess.")
    else:
        print("You are out of guesses.You loose.")
        game_on=False
    
