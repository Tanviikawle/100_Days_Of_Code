import os

def highest_bitter(members):
    highest_value=0
    for member in members:
        amount=int(members[member])
        if amount>highest_value:
            highest_value=amount
            winner=member
        
    os.system('cls')
    print(f"The highest bid is ${highest_value} and the winner is {winner}")

print('''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
''')

print("Welcome to secret auction !")
more =True
new_member={}

while more:
    name=input("Enter your name: ")
    value=input("What's your bit: $")
    new_member[name]=value
    more_member=input("are there any more bidders? Type \'yes' or 'no\'").lower()
    if more_member=="yes":
        os.system('cls')
    else:
        highest_bitter(new_member)
        more=False