import logging
import time

import coloredlogs
import schedule

from clients import csv_client as cc
from clients import web_client as wc

coloredlogs.install(level='DEBUG')
logger = logging.getLogger(__name__)


def option_chain_data():
    # logger.info('Starting option chain data')
    # logger.debug('Starting option chain data')
    # logger.warning('Starting option chain data')
    # logger.error('Starting option chain data')
    # logger.critical('Starting option chain data')
    json_file_status = wc.option_chain_data()
    logger.info('From webclient: {}'.format(json_file_status))
    logger.info("===========================================================================")

    if json_file_status.startswith("CREATED"):
        created_csv = cc.create_csv("json/oc-NIFTY-16-11-2021-15-32.json")
    #     print(created_csv)
    else:
        logger.warning("No Data from NSE")


if __name__ == "__main__":
    schedule.every(4).seconds.do(option_chain_data)
    while True:
        schedule.run_pending()
        time.sleep(1)
        print("3")
