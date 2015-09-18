from urllib.request import urlopen
from lxml import etree
import functools

url_fmt = 'http://www.timeanddate.com/scripts/dateserver.php?mode=workdays&d1={day_start}&m1={month_start}&y1={year_start}&d2={day_end}&m2={month_end}&y2={year_end}&ti=&atyp=0&ach=3'
xpath = '/html/body/div[1]/div/div[1]/h2/text()'

@functools.lru_cache(maxsize=None)
def get_days_left(year_start, month_start, day_start, year_end, month_end, day_end):
    url = url_fmt.format(
        year_start=year_start,
        month_start=month_start,
        day_start=day_start,
        year_end=year_end,
        month_end=month_end,
        day_end=day_end)
    response = urlopen(url)
    htmlparser = etree.HTMLParser()
    tree = etree.parse(response, htmlparser)
    result = tree.xpath(xpath)[0]
    days_left = result.split(':')[1].strip().split(' ')[0]
    return int(days_left)


