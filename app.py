import os
from flask import (
    Flask,
    jsonify,
    request
)
from days import get_days_left
import sys

app = Flask(__name__)

@app.route('/')
def hello():
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')
    result = get_days_left(year, month, day)
    return jsonify({
        'days': result
    })

if __name__ == '__main__':
    app.run(debug=True)
