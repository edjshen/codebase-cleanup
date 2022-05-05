

print("STOCKS REPORT...")

import os
from dotenv import load_dotenv
from pandas import read_csv
from alphavantage_api import *

load_dotenv()

ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")
symbol = input("Please input a crypto symbol (default: 'NFLX'): ") or "NFLX"
df = pullstocks(symbol)
#print(df.columns)
#breakpoint()

latest = df.iloc[0]

print(symbol)
print(latest["timestamp"])
print(latest["close"])
print('${:,.2f}'.format(latest["close"]))
