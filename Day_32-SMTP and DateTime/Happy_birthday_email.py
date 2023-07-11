from datetime import datetime
import smtplib
import pandas
import random

MY_EMAIL="mailt6419@gmail.com"
MY_PASSWORD="abcdefu123"

today=datetime.now()
today_tuple=(today.month,today.year)

data=pandas.read_csv("C:/Users/Ashlesha/Documents/Projects/Python Projects #100DaysOfCode/Day_32-SMTP and DateTime/birthdays.csv")
birthdays_dict={(data_row["month"],data_row["day"]):data_row for (index,data_row) in data.items()}
if today_tuple in birthdays_dict:
    birthday_person=birthdays_dict[today_tuple]
    file_path=f"C:/Users/Ashlesha/Documents/Projects/Python Projects #100DaysOfCode/Day_32SMTP and DateTime/letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents=letter_file.read()
        contents=contents.replace("[NAME]",birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL,MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )