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
  first_currency = data['data'][0]
  print(first_currency)
except (ConnectionError, Timeout, TooManyRedirects) as e:
  print(e)

# app = Flask(__name__)




# if __name__ == '__main__':
#     app.run(debug = True)

