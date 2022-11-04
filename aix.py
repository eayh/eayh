import time
import requests
import csv
from time import gmtime
import time
from datetime import datetime



f=open('log.csv','w',newline='')
writer=csv.writer(f)
writer.writerow(['price','quantity','type','timestamp'])


response=requests.get('https://api.bithumb.com/public/orderbook/BTC_KRW/?count=10')
response=response.json()
n=0
timestamp=response['data']['timestamp']

timestamp=float(timestamp)/1000
timestamp=timestamp
for i in response['data']['bids']:
    if n<5:
        data=[i['price'],i['quantity'],0,datetime.fromtimestamp(timestamp, tz=None)]
        writer.writerow(data)
    n=n+1
n=0
for i in response['data']['asks']:
    if n<5:
        data=[i['price'],i['quantity'],1,datetime.fromtimestamp(timestamp, tz=None).strftime("%Y-%m-%d %H:%M:%S.%f")]
        writer.writerow(data)
    n=n+1



while(1):
    try:
        time.sleep(3)
        response = requests.get('https://api.bithumb.com/public/orderbook/BTC_KRW/?count=10')
        response = response.json()
        print(datetime.fromtimestamp(timestamp, tz=None).strftime("%Y-%m-%d %H:%M:%S.%f"))

        n = 0
        timestamp = response['data']['timestamp']
        timestamp = float(timestamp) / 1000
        timestamp = timestamp
        for i in response['data']['bids']:
            if n < 5:


                    data = [i['price'], i['quantity'], 0, datetime.fromtimestamp(timestamp, tz=None).strftime("%Y-%m-%d %H:%M:%S.%f")]

                    writer.writerow(data)
            n = n + 1
        n = 0

        for i in response['data']['asks']:
                if n < 5:

                    data = [i['price'], i['quantity'], 1, datetime.fromtimestamp(timestamp, tz=None).strftime("%Y-%m-%d %H:%M:%S.%f")]

                    writer.writerow(data)
                n = n + 1
    except:
        pass
