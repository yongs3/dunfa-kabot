from flask import Flask, jsonify

app = Flask(__name__)

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
    app.run(debug=True)