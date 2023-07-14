import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY="R8S7N2U2X8R5XNSC"
NEWS_API_KEY="6b9cafaff6af450f92693eec9509db04"

parameters={
    "function":"TIME_SERIES_DAILY_ADJUSTED",
    "symbol":STOCK,
    "apikey":API_KEY
}

news_params={
    "q":COMPANY_NAME,
    "apiKey":NEWS_API_KEY
}

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = f'https://www.alphavantage.co/query'
r = requests.get(url,params=parameters)
data = r.json()

data_list=[value for(key,value) in data.items()]

dict_data=data_list[1]

dict_data=[value for(key,value) in dict_data.items()]
yesterday_close_price=dict_data[0]["4. close"]
previous_close_price=dict_data[1]["4. close"]

difference=float(yesterday_close_price)-float(previous_close_price)

if difference>0:
    up_down="🔺"
else:
    up_down="🔻"

diff_percentage=round((difference/float(yesterday_close_price))*100)

if abs(diff_percentage)>5:
    print("Get news")


response=requests.get(url="https://newsapi.org/v2/everything",params=news_params)
news_data=response.json()["articles"]
articles=news_data[:3]


formatted_article_list= [f"{STOCK}: {up_down}{diff_percentage}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in articles]


account_sid = 'AC97feeed94f0cec5d50c6b41797ccbf21'
auth_token = '6e23a82e895d10fe31e159251825ccd6'
client = Client(account_sid, auth_token)

for article in formatted_article_list:
    message = client.messages.create(
    from_='+18149292411',
    to='+919326154365',
    body=article
    )



