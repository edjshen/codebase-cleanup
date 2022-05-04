# -*- coding: utf-8 -*-
"""
Created on Wed May  4 18:08:02 2022

@author: edjsh
"""
import os
import json
from dotenv import load_dotenv
import requests

def pull():

    load_dotenv()

    ALPHAVANTAGE_API_KEY = os.getenv("ALPHAVANTAGE_API_KEY", default="demo")

    # docs: https://www.alphavantage.co/documentation/#unemployment
    url = f"https://www.alphavantage.co/query?function=UNEMPLOYMENT&apikey={ALPHAVANTAGE_API_KEY}"
    response = requests.get(url)
    parsed_response = json.loads(response.text)
    #print(parsed_response)

    data = parsed_response["data"]
    latest = data[0]
    return data
