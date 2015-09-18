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
    bg = '#' + request.args.get('bg', 'a1a1a1')
    fg = '#' + request.args.get('fg', '000000')
    highlight = '#' + request.args.get('highlight', 'e9ab17')
    size = request.args.get('size', '14')
    if not what:
        return {}
    else:
        today = dt.date.today()
        result = get_days_left(
                year_start=today.year,
                month_start=today.month,
                day_start=today.day,
                year_end=request.args.get('year'),
                month_end=request.args.get('month'),
                day_end=request.args.get('day'))
        dic = {
            'days': result,
            'what': what,
            'bg': bg,
            'fg': fg,
            'highlight': highlight,
            'size': size
        }
        print(dic)
        return dic

if __name__ == '__main__':
    app.run(debug=True)
