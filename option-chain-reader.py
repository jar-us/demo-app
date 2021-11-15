import json
import requests as webClient
# import nseheader as header
from datetime import datetime
import pandas as pd
import jsonreader as jsonreader
import schedule
import time


def option_chain_data():
    symbol = "nifty"
    date_and_time = datetime.now().strftime("%Y-%m-%d-%H-%M")
    print("Calling NSE Option Chain api at = " + date_and_time)
    file_name = "json/option-chain-" + symbol + "-" + date_and_time + ".json"

    baseurl = "https://www.nseindia.com/"
    url = "https://www.nseindia.com/api/option-chain-indices?symbol=NIFTY"
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                             'like Gecko) '
                             'Chrome/80.0.3987.149 Safari/537.36',
               'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}

    session = webClient.Session()
    request = session.get(baseurl, headers=headers, timeout=5)
    cookies = dict(request.cookies)
    response = session.get(url, headers=headers, cookies=cookies, timeout=5)
    print(response)
    print("Received Response = " + str(response.status_code))

    print("Creating " + file_name + " file")

    jsonWriter = open(file_name, "w")
    jsonWriter.write(json.dumps(response.json()))
    jsonWriter.close()
    response.close()
    print(file_name + " file created")
    jsonreader.writeJsonToCsv(file_name)
    print("Task Over")


while True:
    # schedule.run_pending()
    print("***** Started ******")
    option_chain_data()
    print("***** Completed - Going to sleep for 180 seconds ******")
    time.sleep(180)
