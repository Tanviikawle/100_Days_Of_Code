import smtplib

my_email="mailt6419@gmail.com"
password="abcdefu123"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email,password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="testpython123@myyahoo.com",
        msg="Subject:Hello\n\nThis is the body of my mail."
    )
