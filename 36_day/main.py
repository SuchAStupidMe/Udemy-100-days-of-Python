import requests
from twilio.rest import Client


STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ...
NEWS_API_KEY = ...

TWILIO_SID = ...
TWILIO_AUTH_TOKEN = ...
VIRTUAL_TWILIO_NUMBER = ...
VERIFIED_NUMBER = ...

stock_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': STOCK_NAME,
    'apikey': STOCK_API_KEY
}
response = requests.get(STOCK_ENDPOINT, params=stock_params)
stock_data: dict = response.json()['Time Series (Daily)']
data_list = [value for (key, value) in stock_data.items()]

yesterday_closing_price = data_list[0]['4. close']
day_before_yesterday_closing_price = data_list[1]['4. close']

difference = abs(float(yesterday_closing_price) - float(day_before_yesterday_closing_price))
diff_percent = (difference / float(yesterday_closing_price)) * 100

up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

if diff_percent > 5:
    news_params = {
        'apiKey': NEWS_API_KEY,
        'qInTitle': COMPANY_NAME
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()['articles'][:3]

    news_list = formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}" for article in articles]

    client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    for article in news_list:
        message = client.messages.create(
            body=article,
            from_=VIRTUAL_TWILIO_NUMBER,
            to=VERIFIED_NUMBER
        )



