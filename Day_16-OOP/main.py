from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

order=Menu()
coffee=CoffeeMaker()
amount=MoneyMachine()


flag=True
while flag:
    drink=input(f"What would you like? {order.get_items()}: ")

    if drink=="off":
        print("Machine turned off.")
        flag=False
    elif drink=="report":
        coffee.report()
        amount.report() 
    else:
        choice=order.find_drink(drink)
        if coffee.is_resource_sufficient(choice) and amount.make_payment(choice.cost):
            coffee.make_coffee(choice)