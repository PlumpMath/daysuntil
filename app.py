from flask import (
    Flask,
    request
)
from days import get_days_left
from flask.ext.pushrod import Pushrod, pushrod_view
import datetime as dt

app = Flask(__name__)
Pushrod(app)

@app.route('/')
@pushrod_view(jinja_template='index.html')
def hello():
    what = request.args.get('what')
    if not what:
        return {}
    else:
        cache = dt.date.today().strftime('%Y-%m-%d')
        result = get_days_left(cache,
                request.args.get('year'),
                request.args.get('month'),
                request.args.get('day'))
        return {
            'days': result,
            'what': what
        }

if __name__ == '__main__':
    app.run(debug=True)
