from urllib.request import urlopen
from lxml import etree
import functools

url_fmt = 'http://www.timeanddate.com/scripts/dateserver.php?mode=workdays&d1=14&m1=9&y1=2015&d2={day}&m2={month}&y2={year}&ti=&atyp=0&ach=3'
xpath = '/html/body/div[1]/div/div[1]/h2/text()'

@functools.lru_cache(maxsize=None)
def get_days_left(cache_key, year, month, day):
    url = url_fmt.format(year=year, month=month, day=day)
    response = urlopen(url)
    htmlparser = etree.HTMLParser()
    tree = etree.parse(response, htmlparser)
    result = tree.xpath(xpath)[0]
    days_left = result.split(':')[1].strip().split(' ')[0]
    return int(days_left)


