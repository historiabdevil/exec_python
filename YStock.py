class YStock:
    URL_CURRENT='http://finace.yahoo.com/d/quotes.csv?s=%(symbol)s&f=%(columns)s'
    URL_HISTORICAL='http://ichart.yahoo.com/table.csv?s=%(s)s&a=%(a)s&b=%(b)s&c=%(c)s&d=%(d)s&e=%(e)s&f=%(f)s'
    def __init__(self, symbol):
        self.symbol = symbol
    def current(self):
        import urllib
        FIELDS=(('price','l1'),
        ('change','c1'),
        ('volume','v'),
        ('average_daily_volume','a2'),
        ('stock_exchange','x'),
        ('market_cap','j1'))
        columns = ''.join([row[1] for row in FIELDS])
        url = self.URL_CURRENT % dict(symbol=self.symbol, columns=columns)
        raw_data = urllib.urlopen(url).read().strip().strip('"').split(',')
        current=dict()
        for i, row in enumerate(FIELDS):
            try:
                current[row[0]] = float(raw_data[i])
            except:
                current[row[0]] = raw_data[i]
        return current
    def historical(self, start=None, stop=None):
        import datetime, time, urllib, math
        start = start or datetime.date(1900, 1, 1)
        stop = stop or datetime.today()
        url = self.URL_HISTORICAL % dict(s=self.symbol, a = start.month-1, b=start.day, c=start.year, d=stop.month-1, e=stop.day, f=stop.year)
        lines = urllib.urlopen(url).readlines()
        raw_data=[row.split(',') for row in line[1:] if row.count(',') == 6]
        previous_adjusted_close = 0
        series = []
        raw_data.reverse()
        for row in raw_data:
            open, high, low = float(row[1]), float(row[2]), float(row[3])
            close, vol = float(row[4]), float(row[5])
            adjusted_close=float(row[6])
            adjustment = adjusted_close / close
            if previous_adjusted_close:
                arithmetic_return = adjusted_close/previous_adjusted_close-1.0
                log_return = math.log(adjusted_close/previous_adjusted_close)
            else:
                arithmetic_return=log_return=None
                previous_adjusted_close = adjusted_close
                series.append(dict(date=datetime.datetime.strptime(row[0], '%Y-%m-%d'),
                open = open,
                high = high,
                low = low,
                close = close,
                volume = vol,
                adjusted_close = adjusted_close,
                adjusted_open = open*adjustment,
                adjusted_high = high*adjustment,
                adjusted_low = low*adjustment,
                adjusted_vol = vol/adjustment,
                arithmetic_return = arithmetic_return,
                log_return = log_return))
        return series

    @staticmethod
    def download(symbol='goog', what='adjusted_close', start=None, stop=None):
        return [d[what] for d in YStock(symbol).historical(start, stop)]
download()
