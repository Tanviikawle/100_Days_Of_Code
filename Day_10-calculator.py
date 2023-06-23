# import os 

# #addition
# def add(n1,n2):
#     return n1+n2

# #subtraction
# def sub(n1,n2):
#     return n1-n2

# #multiplication
# def mul(n1,n2):
#     return n1*n2

# #division
# def div(n1,n2):
#     return n1/n2
    
# #modulus
# def mod(n1,n2):
#     return n1%n2
    
# def calculator():
#     flag=True
#     operation={"+":add,
#                 "-":sub,
#                 "*":mul,
#                 "/":div,
#                 "%":mod}
#     print('''
#          _____________________
#         |  _________________  |
#         | | JO           0. | |
#         | |_________________| |
#         |  ___ ___ ___   ___  |
#         | | 7 | 8 | 9 | | + | |        ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ ___ 
#         | |___|___|___| |___| |       / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__/ __|
#         | | 4 | 5 | 6 | | - | |      | (_| (_| | | (__| |_| | | (_| | || (_) | |  \__ \\
#         | |___|___|___| |___| |       \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|  |___/
#         | | 1 | 2 | 3 | | x | |
#         | |___|___|___| |___| |
#         | | . | 0 | = | | / | |
#         | |___|___|___| |___| |
#         |_____________________|
        
#     ''')
#     num1=float(input("Enter 1st number: "))
    
#     for symbol in operation:
#         print(symbol)
#     while flag:
#         if flag:
#             op=input("Select an operator from line above: ")
#             num2=float(input("Enter 2nd number: "))
        
#             calculation=operation[op]
#             result=calculation(num1,num2)
#             print(f"{num1} {op} {num2} = {result}")
#             decision=input(f"Type'y' to continue calculation with {result} , or type 'n' to exit: ")
#         if decision=="y":
#             num1=result
#         else:
#             flag=False
#             os.system('cls')
#             calculator()
            
# calculator()


import os

def add(n1,n2):
    return (n1+n2)

def sub(n1,n2):
    return (n1-n2)

def mul(n1,n2):
    return (n1*n2)

def div(n1,n2):
    return (n1/n2)

def mod(n1,n2):
    return (n1%n2)


def calculator():
    operation={
        "+":add,
        "-":sub,
        "*":mul,
        "/":div,
        "%":mod,
    }

    print('''
         _____________________
        |  _________________  |
        | | JO           0. | |
        | |_________________| |
        |  ___ ___ ___   ___  |
        | | 7 | 8 | 9 | | + | |        ___ __ _| | ___ _   _| | __ _| |_ ___  _ __ ___ 
        | |___|___|___| |___| |       / __/ _` | |/ __| | | | |/ _` | __/ _ \| '__/ __|
        | | 4 | 5 | 6 | | - | |      | (_| (_| | | (__| |_| | | (_| | || (_) | |  \__ \\
        | |___|___|___| |___| |       \___\__,_|_|\___|\__,_|_|\__,_|\__\___/|_|  |___/
        | | 1 | 2 | 3 | | x | |
        | |___|___|___| |___| |
        | | . | 0 | = | | / | |
        | |___|___|___| |___| |
        |_____________________|
        
    ''')

    num1=float(input("Enter 1st number: "))
    again=True
    while again:
        for op in operation:
            print(op)
        symbol=input("Select an operator from line above: ")
        num2=float(input("Enter 2nd number: "))
        func=operation[symbol]
        result=func(num1,num2)
        print(f"{num1} {symbol} {num2} = {result}")
        decision=input(f"Type'y' to continue calculation with {result} , or type 'n' to exit: ")
        if decision=="n":
            os.system('cls')
            again=False
            calculator()
        else:
            num1=result

        
calculator()


