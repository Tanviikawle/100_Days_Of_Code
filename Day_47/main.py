import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL="https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
MY_EMAIL="mailt6419@gmail.com"
MY_PASSWORD="abcdefu123"

header={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36",
    "Accept-Language":"en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6"
}

response=requests.get(url=URL,headers=header)
# print(response.content)
website_html=response.content

soup=BeautifulSoup(website_html,"lxml")

price=soup.find(name="span",class_="a-color-success").getText()
title=soup.find(name="span",id="productTitle").getText()
print(title)

price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

BUY_PRICE = 200

if price_as_float < BUY_PRICE:
    message = f"{title} is now {price}"

    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
            connection.starttls()
            connection.login(MY_EMAIL,MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=MY_EMAIL,
                msg=f"Subject:Amazon Price Alert!\n\n{message}\n{URL}".encode("utf-8")
            )