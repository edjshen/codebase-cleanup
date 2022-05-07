


print("CRYPTO REPORT...")

import os
import json
from dotenv import load_dotenv
import requests
from alphavantage_api import *
from utils import *

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")
symbol = input("Please input a crypto symbol (default: 'BTC'): ") or "BTC"

tsd = pullcrypto(symbol)

#print(latest)
# not sure about the difference between '4a. close (USD)' and '4b. close (USD)'

dates = list(tsd.keys())
latest_date = dates[0]
latest = tsd[latest_date]

print(symbol)
print(latest_date)
print(latest['4a. close (USD)'])
print('${:,.2f}'.format(float(latest['4a. close (USD)'])))
