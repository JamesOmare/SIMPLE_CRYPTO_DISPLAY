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
                'X-CMC_PRO_API_KEY': os.environ.get('X-CMC_PRO_API_KEY')
            }

            session = Session()
            session.headers.update(headers)

            try:
                response = session.get(url, params=parameters)
                data = json.loads(response.text)
                formated_data = data.get('data')
                print(formated_data)
                
            except (ConnectionError, Timeout, TooManyRedirects) as e:
                print('Error in api call', e)

            
        else:
            return redirect(url_for('crypto.rebound'))
    

    return render_template(
        'coins.html', 
        _data= formated_data,
        )

@crypto.get('/no_data')
def rebound():
    return render_template('error.html')