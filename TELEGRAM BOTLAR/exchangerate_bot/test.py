import requests

response = requests.get('https://v6.exchangerate-api.com/v6/bf014e36e890306180fb2b47/pair/USD/UZS')
print(response.json()['conversion_rate'])