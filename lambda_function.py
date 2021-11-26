from datetime import datetime as dt

import boto3 as boto3

import requests as rq


def get_property_value_from_json(json_object, property_name):
    return json_object['records'][property_name]


def option_chain_data(event=None, context=None):
    symbol = "NIFTY"
    baseurl = "https://www.nseindia.com/"
    url = "https://www.nseindia.com/api/option-chain-indices?symbol=" + symbol
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                             'like Gecko) '
                             'Chrome/80.0.3987.149 Safari/537.36',
               'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}

    session = rq.Session()
    request = session.get(baseurl, headers=headers, timeout=120)
    cookies = dict(request.cookies)

    response = session.get(url, headers=headers, cookies=cookies, timeout=120)

    if (response.status_code == 200) & (response.text != "") & (response.text != "[]"):
        time_stamp_res = dt.strptime(get_property_value_from_json(response.json(), "timestamp"), "%d-%b-%Y %H:%M:%S")
        last_updated_date = str(dt.strftime(time_stamp_res, "%d-%b-%Y"))
        last_updated_time = str(dt.strftime(time_stamp_res, "%H:%M:%S"))
        aws_s3_client(last_updated_date, last_updated_time, response)


def aws_s3_client(last_updated_date, last_updated_time, response):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket('nse.options.chain.nifty.json')
    bucket.put_object(Key=last_updated_date + "/" + last_updated_time, Body=response.text)


if __name__ == "__main__":
    try:
        option_chain_data()
    except Exception as e:
        print("Error in option chain data: " + str(e))
    finally:
        print("Option chain data completed")
