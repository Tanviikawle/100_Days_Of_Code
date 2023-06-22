import random

words=["apple","banana","mango","cherry","pineapple","blueberry","grape","guava"]
wrd=random.choice(words)
lenght=len(wrd)
from art import stage;

print('''
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       ''')

mylist=[]
i=0
j=0

while i<lenght:
    mylist.append("_")
    i+=1

end=False
lives=6

while not end:  
    x= input("Guess a letter: ").lower()
    if x in mylist:
        print(f"You've already guessed {x}.")
    for position in range(lenght):
        letter=wrd[position]
        if letter==x:
            mylist[position]=letter
    print(mylist)

    if "_" not in mylist:
        end=True
        print("You Win!!!")
        break
    elif x not in wrd:
        print("You made wrong choice , you loose one life.")
        lives-=1
        if lives==0:
            print(stage[lives])
            print("You loose!")
            break

    print(stage[lives])
    