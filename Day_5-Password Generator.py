import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password generator!")
chars=int(input(f"How many letters would you like in your passoword? \n"))
nums=int(input(f"How many numbers would you like? \n"))
sybs=int(input(f"How many symbols would you like? \n"))

pass_list=[]
for char in range(1,chars+1):
    pass_list.append(random.choice(letters))

for char in range(1,nums+1):
    pass_list += random.choice(numbers)

for char in range(1,sybs+1):
    pass_list += random.choice(symbols)

random.shuffle(pass_list)

password=""
for char in pass_list:
    password+=char

print(f"Your password is : {password}")

