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
        cache = dt.date.today().strftime('%Y-%m-%d')
        result = get_days_left(cache,
                request.args.get('year'),
                request.args.get('month'),
                request.args.get('day'))
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
