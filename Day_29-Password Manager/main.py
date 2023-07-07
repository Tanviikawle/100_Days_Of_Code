from tkinter import *
from tkinter import messagebox
import random
import pyperclip


def generate_pass():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list=[]

    password_letters=[random.choice(letters) for char in range(random.randint(8,10))]
    password_symbols=[random.choice(symbols) for char in range(random.randint(2,4))]
    password_numbers=[random.choice(numbers) for char in range(random.randint(2,4))]

    password_list=password_letters+password_symbols+password_numbers
    random.shuffle(password_list)
    final_password="".join(password_list)

    pass_entry.insert(0,final_password)
    pyperclip.copy(final_password)



def add_data():
    web=web_entry.get()
    email=email_entry.get()
    password=pass_entry.get()

    if len(web)==0 or len(password)==0:
        messagebox.showinfo(title="Oops!",message="Please mkesure that you haven't left any field empty.")

    else:
        output=messagebox.askokcancel(title={web},message=f"These are the details entered: \nEmail: {email}\nPassword: {password}\nIs it okay to save?")

    if output:
        with open("C:/Users/Ashlesha/Documents/Projects/Python Projects #100DaysOfCode/Day_29-Password Manager/data.txt","a")as f:
            data=f"{web}|{email}|{password}\n"
            f.write(data)
            web_entry.delete(0,END)
            pass_entry.delete(0,END)

        

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas=Canvas()
lock_img=PhotoImage(file="C:/Users/Ashlesha/Documents/Projects/Python Projects #100DaysOfCode/Day_29-Password Manager/logo.png")
canvas.create_image(100,100 ,image=lock_img)
canvas.grid(row=0,column=1)

website_label=Label(text="Website:")
website_label.grid(row=1,column=0)
email_label=Label(text="Email/Username:")
email_label.grid(row=2,column=0)
pass_label=Label(text="Password:")
pass_label.grid(row=3,column=0)

web_entry=Entry(width=35)
web_entry.grid(row=1,column=1,columnspan=2)
web_entry.focus()
email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"Examle@gmail.com")
pass_entry=Entry(width=21)
pass_entry.grid(row=3,column=1)

generate=Button(text="Generte password",command=generate_pass)
generate.grid(row=3,column=2)

add_button=Button(text="Add",width=36,command=add_data)
add_button.grid(row=4,column=1,columnspan=2)







window.mainloop()