from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
parameters = {
  'start':'1',
  'limit':'5',
  'convert':'USD'
}
headers = {
  'Accepts': 'application/json',
  'X-CMC_PRO_API_KEY': 'def505b9-ad4f-46fc-9fba-e6686c27a579',
}

session = Session()
session.headers.update(headers)

try:
  response = session.get(url, params=parameters)
  data = json.loads(response.text)
  #first_currency = data['data'][0]
  currency_name = data['data'][0]['name']
  currency_symbol = data['data'][0]['symbol']
  currency_slug = data['data'][0]['slug']
  currency_usd_price = data['data'][0]['quote']['USD']['price']
  usd_price = '$'"{:,.2f}".format(currency_usd_price)

  print(usd_price)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

