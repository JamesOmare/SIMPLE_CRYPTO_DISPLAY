from flask import Blueprint, redirect, render_template, request, url_for
from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import json
import os

crypto = Blueprint('crypto', __name__)

@crypto.get('/')
def index():
    return render_template('index.html')

@crypto.route('/coin', methods=['GET','POST'])
def coin():
    if request.method == 'POST':
        if request.form.get('num') != '':
            number = request.form.get('num')
            url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
            parameters = {
                'start':'1',
                'limit':f'{number}',
                'convert':'USD'
            }
            headers = {
                'Accepts': 'application/json',
                'X-CMC_PRO_API_KEY': os.environ['X-CMC_PRO_API_KEY']
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

            except (ConnectionError, Timeout, TooManyRedirects) as e:
                print(e)

            
        else:
            return redirect(url_for('crypto.rebound'))
    

    return render_template(
        'coins.html', 
        _name = currency_name, 
        _symbol = currency_symbol, 
        _slug = currency_slug, 
        _price = usd_price
        )

@crypto.get('/no_data')
def rebound():
    return render_template('error.html')