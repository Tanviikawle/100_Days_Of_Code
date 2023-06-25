MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

from art import logo

print(logo)
print("Welcome to coffee machine!")

#make one function which will print report.
def print_report():
    print(resources)

#make a function to check if resources are enough or not.
def is_enough(drink):
    decision=True
    if MENU[drink]["ingredients"]["water"]>resources["water"]:
        decision=False
        print("Sorry,There is not enough water.")
    if MENU[drink]["ingredients"]["milk"]>resources["milk"]:
        decision=False
        print("Sorry,There is not enough milk.")
    if MENU[drink]["ingredients"]["coffee"]>resources["coffee"]:
        decision=False
        print("Sorry,There is not enough coffee.")
    return decision

#Make function to ask money.
def ask_money(dname):
    print("Insert coins: ")
    quarters = int(input("Enter Number of Quarters: "))
    dimes = int(input("Enter Number of Dimes: "))
    nickels = int(input("Enter Number of Nickels: "))
    pennies = int(input("Enter Number of Pennies: "))

    t = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return t

#Make a function to check whether the transaction was successfull or not.
def make_transaction(drink,amount):
    print(f"You paid: {amount:.2f}")
    if MENU[drink]["cost"]>amount:
        print("Sorry that's not enough money. Money refunded.")
    else:
        change=amount-MENU[drink]["cost"]
        print(f"Here is ${change:.2f} dollars in change.")

def make_drink(drink):
    print(f"Here is your {drink}.")
    resources["water"]-=MENU[drink]["ingredients"]["water"]
    resources["milk"]-=MENU[drink]["ingredients"]["milk"]
    resources["coffee"]-=MENU[drink]["ingredients"]["coffee"]

flag=True
while flag:
    order = input("What would you like? (espresso/latte/cappuccino):").lower()
    if order=="report":
        print_report()
    elif order=="off":
        print("Machine turned off.")
        flag=False
    elif order=="espresso" or order=="latte" or order=="cappuccino":
        if not is_enough(order):
            break
        bill=ask_money(order)
        make_transaction(order,bill)
        make_drink(order)
    else:
        print("Invalid input.")
        
