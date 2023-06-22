import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
art=[rock,paper,scissors]
user_choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print(art[user_choice])
comp_choice=random.randint(0,2)
print(f"Computer chose:\n {art[comp_choice]}" )

if (user_choice>=0 and user_choice<3):
    if (user_choice==0 and comp_choice==2):
        print("You win!")
    elif (user_choice==2 and comp_choice==0):
        print("You loose!")
    elif (user_choice>comp_choice):
        print("You win!")
    elif (user_choice<comp_choice):
        print("You loose!")
    elif(user_choice==comp_choice):
        print("It's draw!")
else:
    print("Invalid input")