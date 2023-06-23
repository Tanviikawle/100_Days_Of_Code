import os
import random

def deal_cards():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    card=random.choice(cards)
    return card


def calculate(cards):
    if sum(cards)==21 and len(cards)==2:
        return 0
    else:
        return sum(cards)
    
def compare(user_score,comp_score):
    if user_score==comp_score:
        print("It's draw.")
    elif user_score>21:
        print("You went over , You loose.")
    elif comp_score>21:
        print("Computer went over, You win.")
    elif user_score==0:
        print("Win with the Blackjack.")
    elif comp_score==0:
        print("You loose, Computer has Blackjack.")
    elif user_score>comp_score:
        print("You win.")
    else:
        print("You lose.")

def play_game():
    user_cards=[]
    comp_cards=[]
    game_over=True

    for crd in range(2):
        user_cards.append(deal_cards())
        comp_cards.append(deal_cards())

    while game_over:
        user_score=calculate(user_cards)
        comp_score=calculate(comp_cards)
        print(f"Your cards are {user_cards} and your score is {user_score}")
        print(f"Opponents first card is {comp_cards[0]}")
        if user_score == 0 or comp_score == 0 or user_score > 21:
          game_over = False
        else:
          user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
          if user_should_deal == "y":
            user_cards.append(deal_cards())
          elif user_score < 17:
            print("Your cards are less than 17. You would have to draw a card")
            user_cards.append(deal_cards())
          else:
            game_over = False

    while comp_score!=0 and comp_score<17:
        comp_cards.append(deal_cards)
        comp_score=calculate(comp_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {comp_cards}, final score: {comp_score}")
    print(compare(user_score, comp_score))

while input('Do you want to play Blackjack? Type "y" to continue and "n" to exit.')=="y":
    os.system("cls")
    play_game()
