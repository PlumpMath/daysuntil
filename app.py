from flask import (
    Flask,
    request
)
from days import get_days_left
from flask.ext.pushrod import Pushrod, pushrod_view

app = Flask(__name__)
Pushrod(app)

@app.route('/')
@pushrod_view(jinja_template='index.html')
def hello():
    year = request.args.get('year')
    month = request.args.get('month')
    day = request.args.get('day')
    what = request.args.get('what')
    result = get_days_left(year, month, day)
    return {
        'days': result,
        'what': what
    }

if __name__ == '__main__':
    app.run(debug=True)
