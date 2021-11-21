import json
import logging
from datetime import datetime as dt

import coloredlogs
import requests as rq

from commons import json_utility as ju
from commons import prop_utility as pu

coloredlogs.install(level='DEBUG')
logger = logging.getLogger(__name__)


def option_chain_data():
    symbol = "NIFTY"
    json_location = "json/oc-"
    baseurl = "https://www.nseindia.com/"
    url = "https://www.nseindia.com/api/option-chain-indices?symbol=" + symbol
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, '
                             'like Gecko) '
                             'Chrome/80.0.3987.149 Safari/537.36',
               'accept-language': 'en,gu;q=0.9,hi;q=0.8', 'accept-encoding': 'gzip, deflate, br'}

    logger.info("Generating Token from NSE..")
    session = rq.Session()
    request = session.get(baseurl, headers=headers, timeout=5)
    cookies = dict(request.cookies)

    logger.info("Token generated. Now pulling Option-Chain API")
    response = session.get(url, headers=headers, cookies=cookies, timeout=5)

    logger.info('Response received from Option-Chain API')

    if (response.status_code == 200) & (response.text != "") & (response.text != "[]"):
        logger.info("Response Status is 200. Response Body is not empty")
        # read timestamp property from demo-app.properties file.
        time_stamp_prop = dt.strptime(pu.get_property_value("demo_app.properties", "timestamp"), "%d-%b-%Y %H:%M:%S")
        time_stamp_res = dt.strptime(ju.get_property_value_from_json(response.json(), "timestamp"), "%d-%b-%Y %H:%M:%S")

        logger.info(
            'Checking Option-Chain API returned data is not older or same than timestamp in demo-app.properties')
        logger.info('TimeStamp in demo-app.properties: ' + str(time_stamp_prop))
        logger.info('TimeStamp in Option-Chain API: ' + str(time_stamp_res))

        if time_stamp_res > time_stamp_prop:
            logger.info('Option-Chain API returned data is newer than timestamp in demo-app.properties')
            # print("timestamp is greater than timestamp in demo-app.properties file")
            file_name = json_location + symbol + "-" + str(time_stamp_res.day) + "-" + str(
                time_stamp_res.month) + "-" + str(time_stamp_res.year) + "-" + str(time_stamp_res.hour) + "-" + str(
                time_stamp_res.minute) + ".json"

            logger.info('Writing Option-Chain API response to file: ' + file_name)

            open(file_name, "x").write(json.dumps(response.json()))

            # print("json file created")
            logger.info('Option-Chain API response written to file: ' + file_name)
            logger.info('Updating timestamp in demo-app.properties file')

            pu.update_property_value("demo_app.properties", "timestamp", time_stamp_res)

            logger.info('Timestamp updated in demo-app.properties file|STATUS=CREATED_' + file_name)
            return "CREATED_" + file_name
        else:
            # print("timestamp is less than timestamp in demo-app.properties file")
            logger.warning(
                'Option-Chain API returned data is older than timestamp in demo-app.properties|STATUS=NOT_CREATED')
            return "NOT_CREATED"
    elif (response.status_code == 200) & (response.text == "") & (response.text == "[]"):
        # print("json file not created")
        logger.warning('Option-Chain API returned data is empty|STATUS=NOT_CREATED')
        return "NOT_CREATED"
    else:
        logger.error('Option-Chain API returned data is not available|STATUS=BLOCKED_NOT_CREATED')
        # print("json file not created")
        return "BLOCKED_NOT_CREATED"
