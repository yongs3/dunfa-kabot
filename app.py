from flask import Flask, jsonify
from dotenv import load_dotenv
import os
import requests
from datetime import datetime, timedelta

load_dotenv()

app = Flask(__name__)

dunfa_api_key = os.getenv('DUNFA_API_KEY')
dunfa_basic_url = 'https://api.neople.co.kr/df/'

def format_datetime(dt):
    return dt.strftime('%Y%m%dT%H%M')

def get_dunfa_timeline(character_info, date_info, limit_info=100, next_info=None):
    dunfa_timeline_url = dunfa_basic_url + 'servers/' + character_info['serverid'] + '/characters/' + character_info['characterid'] + '/timeline'

    params = {
        'limit': limit_info,
        'startDate': date_info['start_date'], 
        'endDate': date_info['end_date']
    }

    if next_info is not None:
        params['next'] = next_info
    
    params['apikey'] = dunfa_api_key

    response = requests.get(dunfa_timeline_url, params=params)

    return response.json()

@app.route('/', methods=['GET'])
def get_data():
    data = {
        'message': '성공',
        'data': {
            'items': [
                {'id': 1, 'name': '상품1', 'price': 1000},
                {'id': 2, 'name': '상품2', 'price': 2000},
                {'id': 3, 'name': '상품3', 'price': 3000}
            ],
            'total': 3
        }
    }
    return jsonify(data)

if __name__ == '__main__':
    # app.run(debug=True)
    print(get_yesterday_date_info())
    print(format_datetime(datetime.now()))