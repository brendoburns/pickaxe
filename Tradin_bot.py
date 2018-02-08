import base64, hashlib, hmac, time, datetime
from requests.auth import AuthBase
from datetime import datetime, timedelta
import requests

#sandbox api base
api_url = 'https://api.gdax.com'

def __date_to_iso8601(date):
      return '{year}-{month:02d}-{day:02d}T{hour:02d}:{minute:02d}:{second:02d}'.format(
      year=date.year,
      month=date.month,
      day=date.day,
      hour=date.hour,
      minute=date.minute,
      second=date.second)


def historical(symbol, start, end, granularity):
    historcalUrl = 'https://api.gdax.com/products/{id}/candles'.format(id=symbol)

   
    pairs = {
        'start': __date_to_iso8601(end),
        'end' : __date_to_iso8601(start),
        'granularity': granularity
    }
   
    response = requests.get(historcalUrl, pairs )
    return response.json()


def getTicker(symbol):

    response = requests.get(api_url + '/products/' + symbol + '/ticker/')

     #check for invalid api response
    if response.status_code is not 200:
        raise Exception('Invalid GDAX STATUS CODE %d' % response.status_code)

    return response.json()

def SMA(period, symbol):
    today = datetime.now()
    endDate = today - timedelta(days=period)
    granularity = 86400

    smaData = historical(symbol, today, endDate, granularity)
    
    totalVol = 0;
    totalPrice = 0;
    for x in range( period):
        totalVol += smaData[x][5]
        totalPrice +=smaData[x][4]

    avgVol = totalVol/period
    avgPrice = totalPrice/period

    smaReturn = {
        'price': avgPrice,
        'volume': avgVol
    }
    
    return smaReturn

start_time = time.time()


SMA(100, 'BTC-USD')
##

##
