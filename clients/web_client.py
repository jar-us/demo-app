import json
from datetime import datetime as dt
import requests as rq


# call nse option chain api
# if response is 200 and body is not empty then:
# before creating json file check if nse option chain data was updated or not.
# read timestamp property from demo-app.properties file.
# timestamp represents last time when nse option chain data was updated.
# fetch timestamp from nse option chain api response then compare if timestamp is greater than timestamp in demo-app.properties file.
# if timestamp is greater than timestamp in demo-app.properties file then create a json file with name: oc-yyyy-mm-dd-mm-ss.json - CREATED -> json file name
# And update timestamp in demo-app.properties file with timestamp from nse option chain api response.
# if timestamp is less than timestamp in demo-app.properties file then dont create a json file. - NOT_CREATED
# if response is 200 and body is empty then dont created json file - NOT_CREATED
# if response is other than 200 then dont create json and return BLOCKED
def option_chain_data():
    symbol = "NIFTY"
    date_and_time = dt.now().strftime("%Y-%m-%d-%H-%M")
    file_name = "json/option-chain-" + symbol + "-" + date_and_time + ".json"
    baseurl = "https://www.nseindia.com/"
    url = "https://www.nseindia.com/api/option-chain-indices?symbol=" + symbol
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                             'like Gecko) '
                             'Chrome/80.0.3987.149 Safari/537.36',
               'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}

    session = rq.Session()
    request = session.get(baseurl, headers=headers, timeout=5)
    cookies = dict(request.cookies)
    response = session.get(url, headers=headers, cookies=cookies, timeout=5)
    print("Received response")
    if (response.status_code == 200) & (response.text != "") & (response.text != "[]"):
        print("Response is 200 and body is not empty")
        # read timestamp property from demo-app.properties file.
        time_stamp_prop = dt.strptime(get_property_value("demo_app.properties", "timestamp"), "%d-%b-%Y %H:%M:%S")
        time_stamp_res = dt.strptime(get_property_value_from_json(response.json(), "timestamp"), "%d-%b-%Y %H:%M:%S")

        if time_stamp_res > time_stamp_prop:
            print("timestamp is greater than timestamp in demo-app.properties file")
            open(file_name, "x").write(json.dumps(response.json()))
            print("json file created")
            update_property_value("demo_app.properties", "timestamp", time_stamp_res)
            print("timestamp updated in demo-app.properties file")
            return "CREATED_" + file_name
        else:
            print("timestamp is less than timestamp in demo-app.properties file")
            return "NOT_CREATED"
    elif (response.status_code == 200) & (response.text == "") & (response.text == "[]"):
        print("json file not created")
        return "NOT_CREATED"
    else:
        print("json file not created")
        return "BLOCKED_NOT_CREATED"


# create a function which should take file and property name as input and return property value.
def get_property_value(file_name, property_name):
    with open(file_name, 'r') as f:
        for line in f:
            if property_name in line:
                return line.split("=")[1].strip()


# # create a function which should take file name and property name and property value as input and update property value.
def update_property_value(file_name, property_name, property_value):
    with open(file_name, "r") as f:
        props = f.readlines()
        with open(file_name, "w") as f:
            for p in props:
                if property_name in p:
                    f.write(property_name + "=" + property_value.strftime("%d-%b-%Y %H:%M:%S") + "\n")


# create a function which should take json object and property name as input and return property value.
def get_property_value_from_json(json_object, property_name):
    return json_object['records']['timestamp']
